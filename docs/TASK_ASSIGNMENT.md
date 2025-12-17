# Task Assignment for Team Members

## 📋 Project: CARPENTER Algorithm Implementation

---

## 👤 Member 1: Data Preprocessing & Input Handling

### Primary File: `src/data_preprocessing.py`

### Tasks:

#### Week 1-2: Core Implementation
- [ ] Implement `load_dataset()` function
  - Support .txt, .csv, .dat formats
  - Handle different delimiters (space, comma, tab)
  - Error handling for missing files
  
- [ ] Implement `preprocess_data()` function
  - Remove duplicate transactions
  - Filter by minimum transaction length
  - Normalize item names (lowercase, trim)
  - Handle empty lines
  
- [ ] Implement `create_transaction_matrix()` function
  - Convert transactions to binary matrix
  - Return item mapping
  - Handle sparse data efficiently
  
- [ ] Implement `transpose_table()` function
  - Transpose transaction matrix
  - Verify correctness
  
- [ ] Implement `get_statistics()` function
  - Count transactions and items
  - Calculate avg/min/max transaction length
  - Calculate database density

#### Week 2-3: Testing & Datasets
- [ ] Create sample datasets
  - Small dataset (100 transactions, 15 items)
  - Medium dataset (500 transactions, 30 items)
  - Large dataset (1000+ transactions, 50+ items)
  
- [ ] Write unit tests (`tests/test_data_preprocessing.py`)
  - Test loading with different formats
  - Test preprocessing functions
  - Test matrix creation
  
- [ ] Document data format in `docs/data_format.md`
  - Explain expected input format
  - Provide examples
  - List supported formats

#### Week 3-4: Integration & Polish
- [ ] Integrate with Member 2's algorithm code
- [ ] Add command-line interface for data loading
- [ ] Create data validation functions
- [ ] Update documentation with examples

### Deliverables:
✅ Working `data_preprocessing.py` module  
✅ At least 3 sample datasets  
✅ Unit tests with >80% coverage  
✅ Documentation: `docs/data_format.md`

---

## 👤 Member 2: CARPENTER Algorithm Core Implementation

### Primary File: `src/carpenter_algorithm.py`

### Tasks:

#### Week 1-2: Core Algorithm
- [ ] Implement `CARPENTER` class initialization
  - Support calculation (percentage or absolute)
  - Parameter validation
  
- [ ] Implement `mine_patterns()` main method
  - Accept transaction or matrix input
  - Calculate minimum support count
  - Orchestrate mining process
  
- [ ] Implement `_find_frequent_items()` function
  - Count support for 1-itemsets
  - Filter by minimum support
  - Sort by support (for efficiency)
  
- [ ] Implement `_calculate_support()` function
  - Use transposed matrix for efficiency
  - Bitwise AND operations
  - Handle empty patterns

#### Week 2-3: Pattern Mining
- [ ] Implement `_mine_closed_patterns()` function
  - Pattern growth strategy (depth-first or breadth-first)
  - Generate candidate patterns
  - Support counting using transposition
  
- [ ] Implement `_is_closed()` function
  - Check if pattern has supersets with same support
  - Optimize closure checking
  - Prune non-closed patterns early
  
- [ ] Implement pruning strategies
  - Early termination for infrequent patterns
  - Avoid redundant pattern generation
  - Use item ordering for efficiency

#### Week 3-4: Optimization & Testing
- [ ] Optimize algorithm performance
  - Profile code to find bottlenecks
  - Optimize support counting
  - Reduce memory usage
  
- [ ] Write unit tests (`tests/test_carpenter_algorithm.py`)
  - Test with known datasets
  - Verify correctness of closed patterns
  - Test edge cases (empty data, high/low support)
  
- [ ] Add complexity analysis documentation
  - Time complexity
  - Space complexity
  - Comparison with other algorithms
  
- [ ] Create algorithm explanation document (`docs/algorithm_explanation.md`)
  - Step-by-step algorithm walkthrough
  - Pseudocode
  - Examples with illustrations

### Deliverables:
✅ Working `carpenter_algorithm.py` module  
✅ Correctly discovers all closed frequent patterns  
✅ Unit tests with >80% coverage  
✅ Documentation: `docs/algorithm_explanation.md`  
✅ Performance benchmarks

---

## 👤 Member 3: Visualization & Analysis

### Primary File: `src/visualization.py`

### Tasks:

#### Week 1-2: Basic Visualizations
- [ ] Implement `PatternVisualizer` class
  - Set up matplotlib/seaborn styling
  - Create consistent color schemes
  
- [ ] Implement `plot_pattern_distribution()` function
  - Bar chart of pattern lengths
  - Clear labels and title
  - Save to results/ folder
  
- [ ] Implement `plot_support_distribution()` function
  - Histogram of support values
  - Mark mean/median lines
  - Save to results/ folder
  
- [ ] Implement `plot_top_patterns()` function
  - Horizontal bar chart of top N patterns
  - Show pattern items and support
  - Clear formatting

#### Week 2-3: Advanced Visualizations
- [ ] Implement `plot_performance_metrics()` function
  - Multi-panel dashboard
  - Execution time, patterns found, support threshold
  - Summary statistics panel
  
- [ ] Implement `plot_comparison()` function
  - Compare multiple algorithm runs
  - Line plots for time vs support, patterns vs support
  - Clear legends and labels
  
- [ ] Implement `create_pattern_heatmap()` function
  - Item co-occurrence matrix
  - Color-coded heatmap
  - Item labels on axes
  
- [ ] Implement `export_patterns_to_csv()` function
  - Convert patterns to DataFrame
  - Clean formatting
  - Include all relevant information

#### Week 3-4: Notebook & Presentation
- [ ] Complete `notebooks/demo.ipynb`
  - Add markdown explanations for each section
  - Ensure all code cells run without errors
  - Add visualizations throughout
  - Include interpretation of results
  
- [ ] Implement `generate_report()` function
  - Text report with all statistics
  - Top patterns list
  - Performance metrics
  - Save to results/ folder
  
- [ ] Write unit tests (`tests/test_visualization.py`)
  - Test plot generation
  - Test export functions
  - Test with edge cases
  
- [ ] Create presentation materials
  - PowerPoint/PDF slides
  - Key findings and insights
  - Visual demonstrations

#### Week 4: Documentation & Final Polish
- [ ] Create visualization gallery in README
- [ ] Add interactive plots (optional: plotly)
- [ ] Create user guide for visualizations
- [ ] Final testing of notebook end-to-end

### Deliverables:
✅ Working `visualization.py` module  
✅ Complete and executable `notebooks/demo.ipynb`  
✅ All visualization functions working  
✅ Generated plots in results/ folder  
✅ Presentation materials  
✅ Unit tests with >80% coverage

---

## 🤝 Shared Responsibilities (All Members)

### Documentation (Continuous)
- Update README.md as project evolves
- Add docstrings to all functions
- Comment complex code sections
- Keep Git commit messages clear

### Testing (Week 3-4)
- Integration testing
- Test with different datasets
- Verify correctness of results
- Performance testing

### Code Review (Continuous)
- Review each other's pull requests
- Provide constructive feedback
- Ensure code quality
- Check for bugs

### Final Integration (Week 4)
- Merge all branches to main
- Test complete pipeline
- Fix integration issues
- Prepare final submission

---

## 📅 Timeline Summary

### Week 1: Foundation
- Member 1: Basic data loading and preprocessing
- Member 2: CARPENTER class skeleton and support counting
- Member 3: Basic visualization setup and plotting functions

### Week 2: Core Features
- Member 1: Complete preprocessing module, create datasets
- Member 2: Implement pattern mining and closure checking
- Member 3: Advanced visualizations and notebook structure

### Week 3: Integration & Testing
- All: Merge features, integration testing
- Member 1: Unit tests and data validation
- Member 2: Algorithm optimization and testing
- Member 3: Complete notebook with analysis

### Week 4: Finalization
- All: Final testing and bug fixes
- All: Documentation completion
- All: Prepare presentation
- All: Final submission

---

## 📊 Progress Tracking

Each member should update this checklist daily:

### Member 1 Progress: ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%
### Member 2 Progress: ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%
### Member 3 Progress: ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0%

---

## 💡 Tips for Success

1. **Communicate daily** - Use WhatsApp/Discord/Slack for quick updates
2. **Commit often** - Push code to GitHub multiple times per day
3. **Review regularly** - Check each other's code weekly
4. **Test early** - Don't wait until the end to test integration
5. **Ask for help** - Stuck? Ask team members or instructor
6. **Meet weekly** - Video call to sync progress and plan next steps

---

## 🚨 Important Dates

- **Week 1 End**: Basic modules working individually
- **Week 2 End**: Core features implemented
- **Week 3 End**: Integration complete, testing done
- **Week 4**: Final polish and submission

---

## 📞 Contact

**Team Communication Channels:**
- GitHub Issues: For task tracking and bugs
- Pull Requests: For code review
- WhatsApp Group: Daily quick updates
- Weekly Meetings: Progress sync

---

**Let's build an amazing CARPENTER implementation! 🛠️**
