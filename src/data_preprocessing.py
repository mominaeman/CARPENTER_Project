import numpy as np
import pandas as pd
from typing import List, Dict, Set, Tuple


class DataLoader:
    # Load and preprocess transactional data for CARPENTER algorithm
    
    def __init__(self, filepath: str = None):
        # Store file path
        self.filepath = filepath
        # List to store all transactions
        self.transactions = []
        # Set to store unique items
        self.items = set()
        # Counter for total transactions
        self.num_transactions = 0
        
    def load_dataset(self, filepath: str = None, delimiter: str = ' ') -> List[Set[str]]:
        # Load transactions from file
        # Update filepath if provided
        if filepath:
            self.filepath = filepath
        
        try:
            # Open and read file
            with open(self.filepath, 'r') as f:
                for line in f:
                    line = line.strip()  # Remove whitespace
                    if line:  # Skip empty lines
                        # Split line into items and convert to set
                        items = set(line.split(delimiter))
                        self.transactions.append(items)
                        # Add items to global item set
                        self.items.update(items)
                        
            self.num_transactions = len(self.transactions)
            print(f"✓ Loaded {self.num_transactions} transactions with {len(self.items)} unique items")
            return self.transactions
            
        except FileNotFoundError:
            print(f"✗ Error: File not found at {self.filepath}")
            return []
        except Exception as e:
            print(f"✗ Error loading dataset: {str(e)}")
            return []
    
    def preprocess_data(self, remove_duplicates: bool = True, 
                       min_transaction_length: int = 1) -> List[Set[str]]:
        # Clean and filter transactions
        if not self.transactions:
            print("✗ No transactions loaded.")
            return []
        
        processed = self.transactions.copy()
        original_count = len(processed)
        
        # Remove duplicate transactions
        if remove_duplicates:
            processed = [set(t) for t in set([frozenset(t) for t in processed])]
            
        # Filter by minimum length
        processed = [t for t in processed if len(t) >= min_transaction_length]
        
        print(f"✓ Preprocessing: {original_count} → {len(processed)} transactions")
        self.transactions = processed
        return processed
    
    def create_transaction_matrix(self) -> Tuple[np.ndarray, List[str], List[int]]:
        # Convert transactions to binary matrix format
        if not self.transactions:
            print("✗ No transactions to convert.")
            return np.array([]), [], []
        
        # Sort items for consistent ordering
        item_list = sorted(list(self.items))
        # Map each item to a column index
        item_to_idx = {item: idx for idx, item in enumerate(item_list)}
        
        # Create empty matrix (all zeros)
        matrix = np.zeros((len(self.transactions), len(item_list)), dtype=int)
        
        # Fill matrix: 1 if item present in transaction, 0 otherwise
        for trans_idx, transaction in enumerate(self.transactions):
            for item in transaction:
                item_idx = item_to_idx[item]
                matrix[trans_idx][item_idx] = 1
                
        transaction_ids = list(range(len(self.transactions)))
        
        print(f"✓ Created transaction matrix: {matrix.shape[0]} × {matrix.shape[1]}")
        return matrix, item_list, transaction_ids
    
    def transpose_table(self, matrix: np.ndarray) -> np.ndarray:
        # Transpose matrix from transaction-based to item-based view
        # Convert rows to columns and vice versa
        transposed = matrix.T
        print(f"✓ Transposed: {matrix.shape} → {transposed.shape}")
        return transposed
    
    def get_statistics(self) -> Dict[str, any]:
        # Calculate dataset statistics
        if not self.transactions:
            return {}
        
        # Get length of each transaction
        transaction_lengths = [len(t) for t in self.transactions]
        
        # Calculate various statistics
        stats = {
            'num_transactions': len(self.transactions),
            'num_unique_items': len(self.items),
            'avg_transaction_length': np.mean(transaction_lengths),
            'min_transaction_length': np.min(transaction_lengths),
            'max_transaction_length': np.max(transaction_lengths),
            'total_items': sum(transaction_lengths),
            'density': sum(transaction_lengths) / (len(self.transactions) * len(self.items))
        }
        
        return stats
    
    def print_statistics(self):
        # Print dataset statistics
        stats = self.get_statistics()
        
        print("\n" + "="*50)
        print("DATASET STATISTICS")
        print("="*50)
        print(f"Total Transactions:     {stats.get('num_transactions', 0)}")
        print(f"Unique Items:           {stats.get('num_unique_items', 0)}")
        print(f"Avg Transaction Length: {stats.get('avg_transaction_length', 0):.2f}")
        print(f"Min Transaction Length: {stats.get('min_transaction_length', 0)}")
        print(f"Max Transaction Length: {stats.get('max_transaction_length', 0)}")
        print(f"Database Density:       {stats.get('density', 0):.4f}")
        print("="*50 + "\n")


def create_sample_dataset(filename: str, num_transactions: int = 100, 
                         num_items: int = 20, avg_length: int = 5):
    # Create a sample dataset for testing
    import random
    
    # Generate list of items
    items = [f"item_{i}" for i in range(1, num_items + 1)]
    
    with open(filename, 'w') as f:
        for _ in range(num_transactions):
            # Random length around average
            length = max(1, int(random.gauss(avg_length, avg_length/3)))
            length = min(length, num_items)
            
            # Pick random items for this transaction
            transaction = random.sample(items, length)
            f.write(' '.join(transaction) + '\n')
    
    print(f"✓ Created sample dataset: {filename}")


# Test the module
if __name__ == "__main__":
    print("Data Preprocessing Module - Member 1")
    print("=" * 50)
    
    # Create sample datasets
    create_sample_dataset('data/raw/sample_small.txt', 
                         num_transactions=50, 
                         num_items=10, 
                         avg_length=4)
    
    create_sample_dataset('data/raw/sample_medium.txt', 
                         num_transactions=500, 
                         num_items=50, 
                         avg_length=8)
    
    # Test loading and preprocessing
    loader = DataLoader()
    transactions = loader.load_dataset('data/raw/sample_small.txt')
    
    if transactions:
        loader.preprocess_data()
        loader.print_statistics()
        
        # Create and transpose matrix
        matrix, items, trans_ids = loader.create_transaction_matrix()
        print(f"\nTransaction Matrix Shape: {matrix.shape}")
        
        transposed = loader.transpose_table(matrix)
        print(f"Transposed Matrix Shape: {transposed.shape}")
