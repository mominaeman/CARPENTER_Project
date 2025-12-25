import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import List, Set, Dict, Tuple


class PatternVisualizer:
    """
    Visualization tools for CARPENTER algorithm results
    Member 3: Ayesha Muniir - Visualization & Analysis
    """
    
    def __init__(self, figsize=(12, 6)):
        self.figsize = figsize
        
    def plot_pattern_support(self, patterns: List[Dict], top_n: int = 15):
        """Plot support values for top N patterns"""
        if not patterns:
            print("No patterns to visualize")
            return
            
        # Sort by support
        sorted_patterns = sorted(patterns, key=lambda x: x.get('support', 0), reverse=True)[:top_n]
        
        pattern_names = [str(p.get('items', set())) for p in sorted_patterns]
        supports = [p.get('support', 0) for p in sorted_patterns]
        
        fig, ax = plt.subplots(figsize=self.figsize)
        bars = ax.barh(range(len(pattern_names)), supports, color='steelblue')
        ax.set_yticks(range(len(pattern_names)))
        ax.set_yticklabels(pattern_names, fontsize=9)
        ax.set_xlabel('Support', fontsize=11)
        ax.set_title(f'Top {top_n} Closed Frequent Patterns by Support', fontsize=12, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
    def plot_pattern_distribution(self, patterns: List[Dict]):
        """Plot distribution of pattern sizes"""
        if not patterns:
            print("No patterns to visualize")
            return
            
        pattern_sizes = [len(p.get('items', set())) for p in patterns]
        supports = [p.get('support', 0) for p in patterns]
        
        fig, ax = plt.subplots(figsize=self.figsize)
        scatter = ax.scatter(pattern_sizes, supports, alpha=0.6, s=100, c=pattern_sizes, cmap='viridis')
        ax.set_xlabel('Pattern Size (# of items)', fontsize=11)
        ax.set_ylabel('Support (# of transactions)', fontsize=11)
        ax.set_title('Closed Frequent Patterns: Size vs Support', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.colorbar(scatter, ax=ax, label='Pattern Size')
        
        plt.tight_layout()
        plt.show()
        
    def plot_transaction_matrix(self, matrix: np.ndarray, item_list: List[str], 
                               sample_size: int = 10):
        """Visualize transaction matrix as heatmap"""
        sample_matrix = matrix[:sample_size, :min(15, len(item_list))]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        im = ax.imshow(sample_matrix, cmap='Blues', aspect='auto')
        
        ax.set_xlabel('Items', fontsize=11)
        ax.set_ylabel('Transactions', fontsize=11)
        ax.set_title('Sample Transaction Matrix', fontsize=12, fontweight='bold')
        ax.set_xticks(range(min(15, len(item_list))))
        ax.set_xticklabels(item_list[:15], rotation=45, ha='right', fontsize=9)
        ax.set_yticks(range(sample_size))
        ax.set_yticklabels([f'T{i+1}' for i in range(sample_size)], fontsize=9)
        
        plt.colorbar(im, ax=ax, label='Present (1) / Absent (0)')
        plt.tight_layout()
        plt.show()
        
    def plot_algorithm_statistics(self, stats: Dict):
        """Plot algorithm execution statistics"""
        if not stats:
            print("No statistics to visualize")
            return
            
        fig, axes = plt.subplots(2, 2, figsize=self.figsize)
        
        # Execution time
        if 'execution_time' in stats:
            axes[0, 0].bar(['Execution Time'], [stats['execution_time']], color='coral')
            axes[0, 0].set_ylabel('Time (seconds)')
            axes[0, 0].set_title('Algorithm Execution Time')
            axes[0, 0].grid(axis='y', alpha=0.3)
        
        # Number of patterns found
        if 'num_patterns' in stats:
            axes[0, 1].bar(['Patterns Found'], [stats['num_patterns']], color='steelblue')
            axes[0, 1].set_ylabel('Count')
            axes[0, 1].set_title('Number of Closed Patterns')
            axes[0, 1].grid(axis='y', alpha=0.3)
        
        # Min support
        if 'min_support' in stats:
            axes[1, 0].text(0.5, 0.5, f"Min Support: {stats['min_support']}", 
                          ha='center', va='center', fontsize=14, 
                          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            axes[1, 0].axis('off')
        
        # Database info
        if 'num_transactions' in stats:
            info_text = f"Transactions: {stats.get('num_transactions', 'N/A')}\n"
            info_text += f"Items: {stats.get('num_items', 'N/A')}"
            axes[1, 1].text(0.5, 0.5, info_text, 
                          ha='center', va='center', fontsize=12,
                          bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
            axes[1, 1].axis('off')
        
        plt.tight_layout()
        plt.show()


# Test the module
if __name__ == "__main__":
    print("Visualization Module - Member 3")
    print("=" * 50)
    print("PatternVisualizer class is ready for use")
