"""
CARPENTER Algorithm Implementation - MEMBER 2 TASK
=================================================

Author: [Member 2 Name]
Description: Core implementation of the CARPENTER algorithm for discovering
             closed frequent itemsets from transactional databases.

Tasks for Member 2:
------------------
1. Implement CARPENTER algorithm core logic
2. Implement closure checking mechanism
3. Implement support counting
4. Implement pattern pruning strategies
5. Optimize for long transactional databases
6. Add time and space complexity documentation
7. Write unit tests in tests/test_carpenter_algorithm.py

Algorithm Overview:
------------------
CARPENTER (Closed pAttern mineR by transPositioN for ExTremely long pattERns)
- Uses transposed table representation
- Discovers closed frequent itemsets efficiently
- Optimized for databases with many transactions but relatively few items
"""

import numpy as np
from typing import List, Set, Dict, Tuple
from collections import defaultdict
import time


class CARPENTER:
    """
    CARPENTER Algorithm Implementation.
    
    The algorithm discovers all closed frequent itemsets from a transactional
    database by utilizing table transposition for efficiency.
    """
    
    def __init__(self, minsup: float = 0.05, use_percentage: bool = True):
        """
        Initialize CARPENTER algorithm.
        
        Args:
            minsup: Minimum support threshold (0-1 if percentage, or absolute count)
            use_percentage: If True, minsup is treated as percentage
            
        Example:
            >>> carpenter = CARPENTER(minsup=0.05)  # 5% minimum support
        """
        self.minsup = minsup
        self.use_percentage = use_percentage
        self.closed_patterns = []
        self.frequent_items = []
        self.total_transactions = 0
        self.min_support_count = 0
        self.execution_time = 0
        
    def mine_patterns(self, 
                     transactions: List[Set[str]] = None,
                     matrix: np.ndarray = None,
                     item_list: List[str] = None) -> List[Dict]:
        """
        Main method to mine closed frequent patterns.
        
        Args:
            transactions: List of transaction sets OR
            matrix: Binary transaction matrix with item_list
            item_list: List of items corresponding to matrix columns
            
        Returns:
            List of closed patterns with their support
            
        TODO for Member 2:
        - Accept either transaction format or matrix format
        - Calculate minimum support count
        - Find frequent items
        - Generate candidate patterns
        - Check closure property
        - Return closed frequent patterns
        """
        start_time = time.time()
        
        # Convert transactions to matrix if needed
        if transactions and not matrix:
            matrix, item_list = self._transactions_to_matrix(transactions)
        
        if matrix is None or item_list is None:
            print("✗ Error: No valid input provided")
            return []
        
        self.total_transactions = matrix.shape[0]
        
        # Calculate minimum support count
        if self.use_percentage:
            self.min_support_count = int(np.ceil(self.minsup * self.total_transactions))
        else:
            self.min_support_count = int(self.minsup)
        
        print(f"Mining closed patterns with minsup = {self.minsup}")
        print(f"Minimum support count: {self.min_support_count}/{self.total_transactions}")
        
        # TODO for Member 2: Implement main algorithm steps
        
        # Step 1: Transpose the table (key insight of CARPENTER)
        transposed_matrix = matrix.T  # Items × Transactions
        
        # Step 2: Find frequent items (1-itemsets)
        self.frequent_items = self._find_frequent_items(matrix, item_list)
        print(f"✓ Found {len(self.frequent_items)} frequent items")
        
        # Step 3: Mine closed patterns using transposed representation
        self.closed_patterns = self._mine_closed_patterns(
            transposed_matrix, 
            item_list, 
            self.frequent_items
        )
        
        self.execution_time = time.time() - start_time
        print(f"✓ Mining complete in {self.execution_time:.2f} seconds")
        print(f"✓ Found {len(self.closed_patterns)} closed frequent patterns")
        
        return self.closed_patterns
    
    def _transactions_to_matrix(self, transactions: List[Set[str]]) -> Tuple[np.ndarray, List[str]]:
        """
        Convert transaction list to binary matrix.
        
        TODO for Member 2:
        - Convert list of sets to binary matrix representation
        """
        all_items = sorted(list(set().union(*transactions)))
        item_to_idx = {item: idx for idx, item in enumerate(all_items)}
        
        matrix = np.zeros((len(transactions), len(all_items)), dtype=int)
        
        for trans_idx, transaction in enumerate(transactions):
            for item in transaction:
                item_idx = item_to_idx[item]
                matrix[trans_idx][item_idx] = 1
        
        return matrix, all_items
    
    def _find_frequent_items(self, matrix: np.ndarray, item_list: List[str]) -> List[Tuple[str, int]]:
        """
        Find all frequent 1-itemsets.
        
        Args:
            matrix: Transaction matrix
            item_list: List of item names
            
        Returns:
            List of tuples (item, support_count)
            
        TODO for Member 2:
        - Count support for each item
        - Filter by minimum support
        - Sort by support (descending) for efficiency
        """
        frequent = []
        
        for idx, item in enumerate(item_list):
            support = np.sum(matrix[:, idx])
            if support >= self.min_support_count:
                frequent.append((item, support))
        
        # Sort by support (descending)
        frequent.sort(key=lambda x: x[1], reverse=True)
        
        return frequent
    
    def _mine_closed_patterns(self, 
                             transposed_matrix: np.ndarray,
                             item_list: List[str],
                             frequent_items: List[Tuple[str, int]]) -> List[Dict]:
        """
        Mine closed frequent patterns using transposed representation.
        
        This is the core of CARPENTER algorithm.
        
        Args:
            transposed_matrix: Transposed transaction matrix (items × transactions)
            item_list: List of all items
            frequent_items: List of frequent items with support
            
        Returns:
            List of closed patterns
            
        TODO for Member 2:
        - Implement pattern growth strategy
        - Use transposed representation for efficient support counting
        - Check closure property before adding pattern
        - Implement pruning strategies
        
        Algorithm Steps:
        1. Start with frequent items as 1-itemsets
        2. Generate candidate k+1-itemsets from k-itemsets
        3. Count support using transposed matrix (fast intersection)
        4. Check if pattern is closed
        5. Add to closed patterns if valid
        """
        closed = []
        
        # Add frequent 1-itemsets that are closed
        for item, support in frequent_items:
            pattern = {item}
            if self._is_closed(pattern, transposed_matrix, item_list):
                closed.append({
                    'pattern': pattern,
                    'support': support,
                    'length': 1
                })
        
        # TODO for Member 2: Implement pattern growth
        # Generate 2-itemsets, 3-itemsets, etc.
        # Use transposed matrix for efficient support counting
        # Check closure before adding to result
        
        # Simplified version - Member 2 should expand this
        closed = self._mine_closed_recursive(
            transposed_matrix, 
            item_list, 
            frequent_items
        )
        
        return closed
    
    def _mine_closed_recursive(self,
                              transposed_matrix: np.ndarray,
                              item_list: List[str],
                              frequent_items: List[Tuple[str, int]],
                              prefix: Set[str] = None,
                              start_idx: int = 0) -> List[Dict]:
        """
        Recursively mine closed patterns (depth-first search approach).
        
        TODO for Member 2:
        - Implement recursive pattern growth
        - Use prefix to avoid duplicate generation
        - Prune search space efficiently
        """
        if prefix is None:
            prefix = set()
        
        closed = []
        
        # Try extending pattern with each frequent item
        for i in range(start_idx, len(frequent_items)):
            item, _ = frequent_items[i]
            new_pattern = prefix | {item}
            
            # Calculate support for new pattern
            support = self._calculate_support(new_pattern, transposed_matrix, item_list)
            
            if support >= self.min_support_count:
                # Check if closed
                if self._is_closed(new_pattern, transposed_matrix, item_list):
                    closed.append({
                        'pattern': new_pattern,
                        'support': support,
                        'length': len(new_pattern)
                    })
                
                # Recursively grow pattern
                # TODO: Add pruning strategies here
                extended = self._mine_closed_recursive(
                    transposed_matrix,
                    item_list,
                    frequent_items,
                    new_pattern,
                    i + 1
                )
                closed.extend(extended)
        
        return closed
    
    def _calculate_support(self, 
                          pattern: Set[str], 
                          transposed_matrix: np.ndarray,
                          item_list: List[str]) -> int:
        """
        Calculate support count for a pattern using transposed matrix.
        
        This is where CARPENTER's efficiency comes from - using transposed
        representation makes support counting faster for long databases.
        
        Args:
            pattern: Set of items
            transposed_matrix: Transposed matrix (items × transactions)
            item_list: List of items
            
        Returns:
            Support count
            
        TODO for Member 2:
        - Find transaction IDs containing all items in pattern
        - Use bitwise AND on transposed rows for efficiency
        """
        if not pattern:
            return 0
        
        # Get indices of items in pattern
        item_to_idx = {item: idx for idx, item in enumerate(item_list)}
        pattern_indices = [item_to_idx[item] for item in pattern if item in item_to_idx]
        
        if not pattern_indices:
            return 0
        
        # Start with first item's transaction set
        result = transposed_matrix[pattern_indices[0]].copy()
        
        # Intersect with other items (bitwise AND)
        for idx in pattern_indices[1:]:
            result = result & transposed_matrix[idx]
        
        # Count transactions containing all items
        support = np.sum(result)
        return support
    
    def _is_closed(self, 
                   pattern: Set[str],
                   transposed_matrix: np.ndarray,
                   item_list: List[str]) -> bool:
        """
        Check if a pattern is closed.
        
        A pattern is closed if no proper superset has the same support.
        
        Args:
            pattern: Set of items to check
            transposed_matrix: Transposed matrix
            item_list: List of all items
            
        Returns:
            True if pattern is closed, False otherwise
            
        TODO for Member 2:
        - Find all supersets of pattern with same support
        - Return False if any superset exists with same support
        - Optimize to avoid checking all possible supersets
        """
        pattern_support = self._calculate_support(pattern, transposed_matrix, item_list)
        
        # Check if any single item can be added without changing support
        for item in item_list:
            if item not in pattern:
                extended_pattern = pattern | {item}
                extended_support = self._calculate_support(extended_pattern, transposed_matrix, item_list)
                
                if extended_support == pattern_support:
                    return False  # Found superset with same support
        
        return True
    
    def get_statistics(self) -> Dict[str, any]:
        """
        Get mining statistics.
        
        Returns:
            Dictionary with statistics
        """
        pattern_lengths = [p['length'] for p in self.closed_patterns]
        
        return {
            'total_closed_patterns': len(self.closed_patterns),
            'execution_time': self.execution_time,
            'min_support_count': self.min_support_count,
            'total_transactions': self.total_transactions,
            'frequent_items': len(self.frequent_items),
            'avg_pattern_length': np.mean(pattern_lengths) if pattern_lengths else 0,
            'max_pattern_length': max(pattern_lengths) if pattern_lengths else 0
        }
    
    def print_patterns(self, limit: int = 10):
        """
        Print discovered closed patterns.
        
        Args:
            limit: Maximum number of patterns to print
        """
        print("\n" + "="*70)
        print("CLOSED FREQUENT PATTERNS")
        print("="*70)
        
        # Sort by support (descending)
        sorted_patterns = sorted(self.closed_patterns, 
                                key=lambda x: x['support'], 
                                reverse=True)
        
        for i, pattern_info in enumerate(sorted_patterns[:limit]):
            pattern = pattern_info['pattern']
            support = pattern_info['support']
            support_pct = (support / self.total_transactions) * 100
            
            print(f"{i+1}. {{{', '.join(sorted(pattern))}}} "
                  f"(support: {support}/{self.total_transactions} = {support_pct:.1f}%)")
        
        if len(sorted_patterns) > limit:
            print(f"\n... and {len(sorted_patterns) - limit} more patterns")
        
        print("="*70 + "\n")


# Example usage and testing
if __name__ == "__main__":
    print("CARPENTER Algorithm Module - Member 2")
    print("=" * 50)
    
    # Create sample transactions for testing
    sample_transactions = [
        {'A', 'B', 'C'},
        {'A', 'B'},
        {'A', 'C'},
        {'B', 'C'},
        {'A', 'B', 'C'},
        {'A', 'B', 'D'},
        {'B', 'C', 'D'},
        {'A', 'B', 'C', 'D'},
    ]
    
    print(f"Sample dataset: {len(sample_transactions)} transactions\n")
    
    # Run CARPENTER algorithm
    carpenter = CARPENTER(minsup=0.4)  # 40% minimum support
    closed_patterns = carpenter.mine_patterns(transactions=sample_transactions)
    
    # Print results
    carpenter.print_patterns()
    
    # Print statistics
    stats = carpenter.get_statistics()
    print("Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
