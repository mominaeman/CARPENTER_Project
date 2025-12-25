from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Set, FrozenSet, Tuple, Optional, Union
import os
import pandas as pd

# ✅ Import Member 1 preprocessing
from data_preprocessing import DataLoader


@dataclass(frozen=True)
class Pattern:
    items: FrozenSet[str]
    support: int


class CARPENTER:
    """
    CARPENTER-style closed frequent itemset mining using a transposed (vertical) representation.

    Input: transactions = List[Set[str]]
    Output: List[Pattern] (closed frequent itemsets)
    """

    def __init__(self, minsup: Union[int, float] = 0.05, max_patterns: Optional[int] = None):
        self.minsup = minsup
        self.max_patterns = max_patterns

        self._n: int = 0
        self._minsup_count: int = 1
        self._all_mask: int = 0
        self._closed: Dict[FrozenSet[str], int] = {}

    def mine_patterns(self, transactions: List[Set[str]]) -> List[Pattern]:
        if not transactions:
            return []

        self._n = len(transactions)
        self._minsup_count = self._normalize_minsup(self.minsup, self._n)
        self._all_mask = (1 << self._n) - 1
        self._closed.clear()

        # 1) Vertical DB: item -> bitmask of transaction IDs
        vdb = self._build_vertical_db(transactions)

        # 2) Keep frequent items
        items: List[Tuple[str, int, int]] = []
        for item, mask in vdb.items():
            sup = mask.bit_count()
            if sup >= self._minsup_count:
                items.append((item, mask, sup))

        # 3) Deterministic sort
        items.sort(key=lambda x: (x[2], x[0]))

        # DFS from empty prefix
        self._dfs(prefix=frozenset(), tidset=self._all_mask, extensions=items)

        out = [Pattern(items=k, support=v) for k, v in self._closed.items()]
        out.sort(key=lambda p: (-len(p.items), -p.support, sorted(p.items)))
        return out

    def _dfs(self, prefix: FrozenSet[str], tidset: int, extensions: List[Tuple[str, int, int]]) -> None:
        if self.max_patterns is not None and len(self._closed) >= self.max_patterns:
            return

        prefix_support = tidset.bit_count()

        # Closure absorption
        closure_items = set()
        kept: List[Tuple[str, int, int]] = []

        for (it, it_mask, _) in extensions:
            proj = tidset & it_mask
            proj_sup = proj.bit_count()
            if proj_sup < self._minsup_count:
                continue
            if proj == tidset:
                closure_items.add(it)
            else:
                kept.append((it, it_mask, proj_sup))

        if closure_items:
            prefix = frozenset(set(prefix) | closure_items)

        if prefix:
            self._add_closed(prefix, prefix_support)

        # Extend recursively
        for idx, (it, it_mask, _) in enumerate(kept):
            new_tid = tidset & it_mask
            new_sup = new_tid.bit_count()
            if new_sup < self._minsup_count:
                continue

            new_prefix = frozenset(set(prefix) | {it})

            new_ext: List[Tuple[str, int, int]] = []
            for (jt, jt_mask, _) in kept[idx + 1:]:
                proj = new_tid & jt_mask
                ps = proj.bit_count()
                if ps >= self._minsup_count:
                    new_ext.append((jt, jt_mask, ps))

            self._dfs(prefix=new_prefix, tidset=new_tid, extensions=new_ext)

            if self.max_patterns is not None and len(self._closed) >= self.max_patterns:
                return

    def _add_closed(self, itemset: FrozenSet[str], support: int) -> None:
        if itemset in self._closed:
            self._closed[itemset] = support
            return

        to_remove = []
        for existing, ex_sup in self._closed.items():
            if ex_sup != support:
                continue
            if existing.issubset(itemset):
                to_remove.append(existing)
            elif itemset.issubset(existing):
                return  # not closed

        for ex in to_remove:
            del self._closed[ex]

        self._closed[itemset] = support

    @staticmethod
    def _normalize_minsup(minsup: Union[int, float], n: int) -> int:
        if isinstance(minsup, float):
            if minsup <= 0 or minsup > 1:
                raise ValueError("minsup as float must be in (0,1].")
            return max(1, int(minsup * n))
        if isinstance(minsup, int):
            if minsup < 1:
                raise ValueError("minsup as int must be >= 1.")
            return minsup
        raise TypeError("minsup must be int or float.")

    @staticmethod
    def _build_vertical_db(transactions: List[Set[str]]) -> Dict[str, int]:
        vdb: Dict[str, int] = {}
        for tid, t in enumerate(transactions):
            bit = 1 << tid
            for item in t:
                vdb[item] = vdb.get(item, 0) | bit
        return vdb


def save_patterns_csv(patterns: List[Pattern], out_path: str = "results/carpenter_patterns.csv") -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    rows = []
    for p in patterns:
        rows.append({
            "items": ",".join(sorted(p.items)),
            "support": p.support,
            "length": len(p.items)
        })

    df = pd.DataFrame(rows)
    df.to_csv(out_path, index=False)
    print(f"✓ Saved patterns to {out_path} ({len(df)} rows)")


if __name__ == "__main__":
    print("CARPENTER Algorithm Module - Member 2")
    print("=" * 50)

    # ✅ Use Member 1 preprocessing pipeline
    loader = DataLoader()
    transactions = loader.load_dataset("data/raw/sample_small.txt")  # adjust dataset name if needed
    transactions = loader.preprocess_data(remove_duplicates=True, min_transaction_length=1)

    if not transactions:
        print("✗ No transactions after preprocessing. Exiting.")
        raise SystemExit(1)

    # ✅ Run CARPENTER
    miner = CARPENTER(minsup=0.05)  # change if teacher gave specific minsup
    patterns = miner.mine_patterns(transactions)

    print(f"✓ Found {len(patterns)} closed frequent patterns")
    for p in patterns[:20]:
        print(f"support={p.support:>4}  items={sorted(p.items)}")

    # ✅ Save for visualization member
    save_patterns_csv(patterns, "results/carpenter_patterns.csv")
