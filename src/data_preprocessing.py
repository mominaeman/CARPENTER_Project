"""
Data Preprocessing Module - MEMBER 1 TASK
==========================================

Author: [Member 1 Name]
Description: This module handles loading, cleaning, and preprocessing 
             of transactional datasets for CARPENTER algorithm.

Tasks for Member 1:
------------------
1. Implement load_dataset() - Load data from various formats
2. Implement preprocess_data() - Clean and format data
3. Implement create_transaction_matrix() - Convert to matrix format
4. Implement data_statistics() - Generate dataset statistics
5. Create sample datasets in data/raw/
6. Add comprehensive docstrings and comments
7. Write unit tests in tests/test_data_preprocessing.py
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Set, Tuple
from collections import defaultdict


class DataLoader:
    """
    Handles loading and preprocessing of transactional data.
    
    Transactional data format:
    - Each line represents one transaction
    - Items in a transaction are separated by spaces or commas
    - Example: "1 2 3 4" or "apple,bread,milk"
    """
    
    def __init__(self, filepath: str = None):
        """
        Initialize the DataLoader.
        
        Args:
            filepath: Path to the dataset file
        """
        self.filepath = filepath
        self.transactions = []
        self.items = set()
        self.num_transactions = 0
        
    def load_dataset(self, filepath: str = None, delimiter: str = ' ') -> List[Set[str]]:
        """
        Load transactional dataset from file.
        
        Args:
            filepath: Path to dataset file (overrides initialized path)
            delimiter: Character separating items (default: space)
            
        Returns:
            List of transactions, where each transaction is a set of items
            
        Example:
            >>> loader = DataLoader()
            >>> transactions = loader.load_dataset('data/raw/retail.txt')
            >>> print(f"Loaded {len(transactions)} transactions")
            
        TODO for Member 1:
        - Handle different file formats (.txt, .csv, .dat)
        - Handle empty lines and malformed data
        - Support different delimiters
        - Add error handling for file not found
        """
        if filepath:
            self.filepath = filepath
            
        # TODO: Implement file loading logic
        # Read file line by line
        # Parse each line into items
        # Store as list of sets
        
        try:
            with open(self.filepath, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:  # Skip empty lines
                        items = set(line.split(delimiter))
                        self.transactions.append(items)
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
    
    def preprocess_data(self, 
                       remove_duplicates: bool = True,
                       min_transaction_length: int = 1) -> List[Set[str]]:
        """
        Clean and preprocess the loaded transactions.
        
        Args:
            remove_duplicates: Remove duplicate transactions
            min_transaction_length: Minimum items per transaction
            
        Returns:
            Preprocessed list of transactions
            
        TODO for Member 1:
        - Remove duplicate transactions
        - Filter short transactions
        - Handle missing values
        - Normalize item names (lowercase, strip whitespace)
        """
        if not self.transactions:
            print("✗ No transactions loaded. Call load_dataset() first.")
            return []
        
        processed = self.transactions.copy()
        original_count = len(processed)
        
        # TODO: Implement preprocessing steps
        # 1. Remove duplicates if requested
        # 2. Filter by minimum length
        # 3. Clean item names
        
        if remove_duplicates:
            # Convert sets to frozensets for hashing, remove duplicates
            processed = [set(t) for t in set([frozenset(t) for t in processed])]
            
        # Filter by minimum length
        processed = [t for t in processed if len(t) >= min_transaction_length]
        
        print(f"✓ Preprocessing: {original_count} → {len(processed)} transactions")
        self.transactions = processed
        return processed
    
    def create_transaction_matrix(self) -> Tuple[np.ndarray, List[str], List[int]]:
        """
        Convert transactions to binary matrix format.
        
        Returns:
            Tuple of (matrix, item_list, transaction_ids)
            - matrix: Binary numpy array (transactions × items)
            - item_list: Ordered list of items
            - transaction_ids: List of transaction IDs
            
        TODO for Member 1:
        - Create binary matrix where matrix[i][j] = 1 if item j in transaction i
        - Return item mapping for interpretation
        - Optimize for sparse data if needed
        """
        if not self.transactions:
            print("✗ No transactions to convert.")
            return np.array([]), [], []
        
        # Create item to index mapping
        item_list = sorted(list(self.items))
        item_to_idx = {item: idx for idx, item in enumerate(item_list)}
        
        # Initialize binary matrix
        matrix = np.zeros((len(self.transactions), len(item_list)), dtype=int)
        
        # Fill matrix
        for trans_idx, transaction in enumerate(self.transactions):
            for item in transaction:
                item_idx = item_to_idx[item]
                matrix[trans_idx][item_idx] = 1
                
        transaction_ids = list(range(len(self.transactions)))
        
        print(f"✓ Created transaction matrix: {matrix.shape[0]} × {matrix.shape[1]}")
        return matrix, item_list, transaction_ids
    
    def transpose_table(self, matrix: np.ndarray) -> np.ndarray:
        """
        Transpose the transaction matrix (key for CARPENTER algorithm).
        
        This converts from transaction-based view to item-based view,
        which is more efficient for long databases.
        
        Args:
            matrix: Transaction matrix (transactions × items)
            
        Returns:
            Transposed matrix (items × transactions)
        """
        transposed = matrix.T
        print(f"✓ Transposed: {matrix.shape} → {transposed.shape}")
        return transposed
    
    def get_statistics(self) -> Dict[str, any]:
        """
        Calculate and return dataset statistics.
        
        Returns:
            Dictionary containing various statistics
            
        TODO for Member 1:
        - Number of transactions
        - Number of unique items
        - Average transaction length
        - Min/max transaction length
        - Item frequency distribution
        """
        if not self.transactions:
            return {}
        
        transaction_lengths = [len(t) for t in self.transactions]
        
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
        """Print dataset statistics in a formatted way."""
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
    """
    Create a sample transactional dataset for testing.
    
    Args:
        filename: Output filename
        num_transactions: Number of transactions to generate
        num_items: Total number of unique items
        avg_length: Average items per transaction
        
    TODO for Member 1:
    - Generate synthetic transactional data
    - Save to file in proper format
    - Create both small and medium-sized datasets
    """
    import random
    
    items = [f"item_{i}" for i in range(1, num_items + 1)]
    
    with open(filename, 'w') as f:
        for _ in range(num_transactions):
            # Random transaction length around average
            length = max(1, int(random.gauss(avg_length, avg_length/3)))
            length = min(length, num_items)
            
            transaction = random.sample(items, length)
            f.write(' '.join(transaction) + '\n')
    
    print(f"✓ Created sample dataset: {filename}")


# Example usage and testing
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
        
        # Create transaction matrix
        matrix, items, trans_ids = loader.create_transaction_matrix()
        print(f"\nTransaction Matrix Shape: {matrix.shape}")
        
        # Transpose for CARPENTER
        transposed = loader.transpose_table(matrix)
        print(f"Transposed Matrix Shape: {transposed.shape}")
