"""
Visualization and Analysis Module - MEMBER 3 TASK
================================================

Author: [Member 3 Name]
Description: Visualization and analysis tools for CARPENTER algorithm results.
             Creates charts, plots, and performance metrics.

Tasks for Member 3:
------------------
1. Implement pattern visualization functions
2. Create performance comparison charts
3. Implement result export functions
4. Create interactive visualizations
5. Generate analysis reports
6. Create comprehensive demo notebook
7. Write unit tests in tests/test_visualization.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Set
import time
from collections import Counter


class PatternVisualizer:
    """
    Visualize closed frequent patterns and algorithm performance.
    """
    
    def __init__(self):
        """Initialize the visualizer with default styling."""
        # Set style for better-looking plots
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        plt.rcParams['font.size'] = 10
        
    def plot_pattern_distribution(self, patterns: List[Dict], save_path: str = None):
        """
        Plot distribution of pattern lengths.
        
        Args:
            patterns: List of pattern dictionaries from CARPENTER
            save_path: Optional path to save the figure
            
        TODO for Member 3:
        - Create bar chart of pattern lengths
        - Show count of patterns for each length
        - Add labels and title
        - Save to results/ folder if path provided
        """
        if not patterns:
            print("✗ No patterns to visualize")
            return
        
        lengths = [p['length'] for p in patterns]
        length_counts = Counter(lengths)
        
        plt.figure(figsize=(10, 6))
        plt.bar(length_counts.keys(), length_counts.values(), color='steelblue', alpha=0.7)
        plt.xlabel('Pattern Length (Number of Items)', fontsize=12)
        plt.ylabel('Number of Patterns', fontsize=12)
        plt.title('Distribution of Closed Pattern Lengths', fontsize=14, fontweight='bold')
        plt.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for length, count in length_counts.items():
            plt.text(length, count, str(count), ha='center', va='bottom')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved pattern distribution plot to {save_path}")
        
        plt.show()
    
    def plot_support_distribution(self, patterns: List[Dict], save_path: str = None):
        """
        Plot distribution of pattern support values.
        
        Args:
            patterns: List of pattern dictionaries
            save_path: Optional path to save figure
            
        TODO for Member 3:
        - Create histogram of support values
        - Show frequency distribution
        - Mark average support line
        """
        if not patterns:
            print("✗ No patterns to visualize")
            return
        
        supports = [p['support'] for p in patterns]
        
        plt.figure(figsize=(10, 6))
        plt.hist(supports, bins=20, color='coral', alpha=0.7, edgecolor='black')
        plt.xlabel('Support Count', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.title('Distribution of Pattern Support Values', fontsize=14, fontweight='bold')
        
        # Add mean line
        mean_support = np.mean(supports)
        plt.axvline(mean_support, color='red', linestyle='--', linewidth=2, 
                   label=f'Mean: {mean_support:.1f}')
        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved support distribution plot to {save_path}")
        
        plt.show()
    
    def plot_top_patterns(self, patterns: List[Dict], top_n: int = 10, save_path: str = None):
        """
        Plot top N patterns by support.
        
        Args:
            patterns: List of pattern dictionaries
            top_n: Number of top patterns to show
            save_path: Optional path to save figure
            
        TODO for Member 3:
        - Sort patterns by support
        - Create horizontal bar chart
        - Show pattern items and support
        """
        if not patterns:
            print("✗ No patterns to visualize")
            return
        
        # Sort by support and take top N
        sorted_patterns = sorted(patterns, key=lambda x: x['support'], reverse=True)[:top_n]
        
        # Prepare data
        pattern_labels = [', '.join(sorted(p['pattern'])) for p in sorted_patterns]
        supports = [p['support'] for p in sorted_patterns]
        
        plt.figure(figsize=(12, 8))
        y_pos = np.arange(len(pattern_labels))
        
        plt.barh(y_pos, supports, color='mediumseagreen', alpha=0.7)
        plt.yticks(y_pos, pattern_labels)
        plt.xlabel('Support Count', fontsize=12)
        plt.ylabel('Patterns', fontsize=12)
        plt.title(f'Top {top_n} Closed Patterns by Support', fontsize=14, fontweight='bold')
        plt.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, v in enumerate(supports):
            plt.text(v, i, f' {v}', va='center')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved top patterns plot to {save_path}")
        
        plt.show()
    
    def plot_performance_metrics(self, metrics: Dict, save_path: str = None):
        """
        Plot performance metrics as a dashboard.
        
        Args:
            metrics: Dictionary of performance metrics
            save_path: Optional path to save figure
            
        TODO for Member 3:
        - Create subplot grid showing different metrics
        - Execution time, memory usage, patterns found, etc.
        - Use various chart types (bar, pie, text)
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('CARPENTER Algorithm Performance Metrics', 
                    fontsize=16, fontweight='bold')
        
        # Metric 1: Execution time
        ax1 = axes[0, 0]
        ax1.bar(['Execution Time'], [metrics.get('execution_time', 0)], 
               color='steelblue', alpha=0.7)
        ax1.set_ylabel('Time (seconds)')
        ax1.set_title('Algorithm Execution Time')
        ax1.grid(axis='y', alpha=0.3)
        
        # Metric 2: Patterns found
        ax2 = axes[0, 1]
        pattern_data = [
            metrics.get('frequent_items', 0),
            metrics.get('total_closed_patterns', 0)
        ]
        ax2.bar(['Frequent Items', 'Closed Patterns'], pattern_data, 
               color=['coral', 'mediumseagreen'], alpha=0.7)
        ax2.set_ylabel('Count')
        ax2.set_title('Patterns Discovered')
        ax2.grid(axis='y', alpha=0.3)
        
        # Metric 3: Support threshold
        ax3 = axes[1, 0]
        support_info = [
            metrics.get('min_support_count', 0),
            metrics.get('total_transactions', 0)
        ]
        ax3.bar(['Min Support', 'Total Transactions'], support_info,
               color=['orange', 'purple'], alpha=0.7)
        ax3.set_ylabel('Count')
        ax3.set_title('Support Threshold vs Database Size')
        ax3.grid(axis='y', alpha=0.3)
        
        # Metric 4: Text summary
        ax4 = axes[1, 1]
        ax4.axis('off')
        summary_text = f"""
        SUMMARY
        {'='*30}
        Total Transactions: {metrics.get('total_transactions', 0)}
        Frequent Items: {metrics.get('frequent_items', 0)}
        Closed Patterns: {metrics.get('total_closed_patterns', 0)}
        
        Min Support Count: {metrics.get('min_support_count', 0)}
        Avg Pattern Length: {metrics.get('avg_pattern_length', 0):.2f}
        Max Pattern Length: {metrics.get('max_pattern_length', 0)}
        
        Execution Time: {metrics.get('execution_time', 0):.2f}s
        """
        ax4.text(0.1, 0.5, summary_text, fontsize=11, family='monospace',
                verticalalignment='center')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved performance metrics to {save_path}")
        
        plt.show()
    
    def plot_comparison(self, results: List[Dict], save_path: str = None):
        """
        Compare multiple CARPENTER runs with different parameters.
        
        Args:
            results: List of result dictionaries with different minsup values
            save_path: Optional path to save figure
            
        TODO for Member 3:
        - Compare execution time vs minsup
        - Compare patterns found vs minsup
        - Create multi-line plot
        """
        if not results:
            print("✗ No results to compare")
            return
        
        minsup_values = [r['minsup'] for r in results]
        execution_times = [r['execution_time'] for r in results]
        pattern_counts = [r['total_closed_patterns'] for r in results]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle('CARPENTER Performance Comparison', fontsize=14, fontweight='bold')
        
        # Plot 1: Execution time vs minsup
        ax1.plot(minsup_values, execution_times, marker='o', color='steelblue', 
                linewidth=2, markersize=8)
        ax1.set_xlabel('Minimum Support Threshold', fontsize=11)
        ax1.set_ylabel('Execution Time (seconds)', fontsize=11)
        ax1.set_title('Execution Time vs Support Threshold')
        ax1.grid(alpha=0.3)
        
        # Plot 2: Patterns found vs minsup
        ax2.plot(minsup_values, pattern_counts, marker='s', color='coral',
                linewidth=2, markersize=8)
        ax2.set_xlabel('Minimum Support Threshold', fontsize=11)
        ax2.set_ylabel('Closed Patterns Found', fontsize=11)
        ax2.set_title('Patterns Discovered vs Support Threshold')
        ax2.grid(alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved comparison plot to {save_path}")
        
        plt.show()
    
    def export_patterns_to_csv(self, patterns: List[Dict], filepath: str):
        """
        Export patterns to CSV file.
        
        Args:
            patterns: List of pattern dictionaries
            filepath: Output CSV file path
            
        TODO for Member 3:
        - Convert patterns to DataFrame
        - Export to CSV with proper formatting
        """
        if not patterns:
            print("✗ No patterns to export")
            return
        
        # Prepare data for DataFrame
        data = []
        for i, p in enumerate(patterns, 1):
            data.append({
                'Pattern_ID': i,
                'Pattern': ', '.join(sorted(p['pattern'])),
                'Length': p['length'],
                'Support': p['support']
            })
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
        print(f"✓ Exported {len(patterns)} patterns to {filepath}")
    
    def create_pattern_heatmap(self, patterns: List[Dict], 
                              item_list: List[str], 
                              save_path: str = None):
        """
        Create heatmap showing item co-occurrence in patterns.
        
        Args:
            patterns: List of pattern dictionaries
            item_list: List of all items
            save_path: Optional path to save figure
            
        TODO for Member 3:
        - Create co-occurrence matrix
        - Visualize as heatmap
        - Show which items frequently appear together
        """
        if not patterns or not item_list:
            print("✗ Insufficient data for heatmap")
            return
        
        # Create co-occurrence matrix
        n_items = len(item_list)
        cooccurrence = np.zeros((n_items, n_items))
        item_to_idx = {item: idx for idx, item in enumerate(item_list)}
        
        for p in patterns:
            items = list(p['pattern'])
            for i in range(len(items)):
                for j in range(len(items)):
                    if i != j:
                        idx_i = item_to_idx.get(items[i])
                        idx_j = item_to_idx.get(items[j])
                        if idx_i is not None and idx_j is not None:
                            cooccurrence[idx_i][idx_j] += 1
        
        # Plot heatmap
        plt.figure(figsize=(12, 10))
        sns.heatmap(cooccurrence, xticklabels=item_list, yticklabels=item_list,
                   cmap='YlOrRd', annot=True, fmt='.0f', cbar_kws={'label': 'Co-occurrence Count'})
        plt.title('Item Co-occurrence in Closed Patterns', fontsize=14, fontweight='bold')
        plt.xlabel('Items', fontsize=12)
        plt.ylabel('Items', fontsize=12)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved heatmap to {save_path}")
        
        plt.show()
    
    def generate_report(self, patterns: List[Dict], metrics: Dict, filepath: str):
        """
        Generate a comprehensive text report.
        
        Args:
            patterns: List of patterns
            metrics: Performance metrics
            filepath: Output file path
            
        TODO for Member 3:
        - Create formatted text report
        - Include all key statistics
        - Save to results/ folder
        """
        with open(filepath, 'w') as f:
            f.write("="*70 + "\n")
            f.write("CARPENTER ALGORITHM - ANALYSIS REPORT\n")
            f.write("="*70 + "\n\n")
            
            f.write("DATASET INFORMATION\n")
            f.write("-" * 70 + "\n")
            f.write(f"Total Transactions: {metrics.get('total_transactions', 0)}\n")
            f.write(f"Minimum Support Count: {metrics.get('min_support_count', 0)}\n")
            f.write(f"Frequent Items Found: {metrics.get('frequent_items', 0)}\n\n")
            
            f.write("PATTERN DISCOVERY RESULTS\n")
            f.write("-" * 70 + "\n")
            f.write(f"Closed Patterns Found: {metrics.get('total_closed_patterns', 0)}\n")
            f.write(f"Average Pattern Length: {metrics.get('avg_pattern_length', 0):.2f}\n")
            f.write(f"Maximum Pattern Length: {metrics.get('max_pattern_length', 0)}\n\n")
            
            f.write("PERFORMANCE METRICS\n")
            f.write("-" * 70 + "\n")
            f.write(f"Execution Time: {metrics.get('execution_time', 0):.2f} seconds\n\n")
            
            f.write("TOP 10 PATTERNS BY SUPPORT\n")
            f.write("-" * 70 + "\n")
            sorted_patterns = sorted(patterns, key=lambda x: x['support'], reverse=True)[:10]
            for i, p in enumerate(sorted_patterns, 1):
                pattern_str = ', '.join(sorted(p['pattern']))
                f.write(f"{i}. {{{pattern_str}}} - Support: {p['support']}\n")
            
            f.write("\n" + "="*70 + "\n")
        
        print(f"✓ Generated report: {filepath}")


# Example usage and testing
if __name__ == "__main__":
    print("Visualization Module - Member 3")
    print("=" * 50)
    
    # Create sample patterns for testing
    sample_patterns = [
        {'pattern': {'A', 'B'}, 'support': 50, 'length': 2},
        {'pattern': {'A', 'C'}, 'support': 45, 'length': 2},
        {'pattern': {'B', 'C'}, 'support': 40, 'length': 2},
        {'pattern': {'A', 'B', 'C'}, 'support': 35, 'length': 3},
        {'pattern': {'A'}, 'support': 60, 'length': 1},
        {'pattern': {'B'}, 'support': 55, 'length': 1},
        {'pattern': {'C'}, 'support': 48, 'length': 1},
        {'pattern': {'A', 'B', 'D'}, 'support': 30, 'length': 3},
    ]
    
    sample_metrics = {
        'total_transactions': 100,
        'min_support_count': 30,
        'frequent_items': 4,
        'total_closed_patterns': 8,
        'avg_pattern_length': 1.875,
        'max_pattern_length': 3,
        'execution_time': 0.152
    }
    
    # Initialize visualizer
    viz = PatternVisualizer()
    
    # Test visualizations
    print("\nGenerating visualizations...")
    viz.plot_pattern_distribution(sample_patterns)
    viz.plot_support_distribution(sample_patterns)
    viz.plot_top_patterns(sample_patterns, top_n=5)
    viz.plot_performance_metrics(sample_metrics)
    
    # Export patterns
    viz.export_patterns_to_csv(sample_patterns, 'results/patterns.csv')
    
    # Generate report
    viz.generate_report(sample_patterns, sample_metrics, 'results/report.txt')
    
    print("\n✓ All visualizations complete!")
