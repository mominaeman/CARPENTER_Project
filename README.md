# CARPENTER Algorithm Implementation
## Closed Pattern Discovery by Transposing Tables that are Extremely Long

### Project Overview
This project implements the CARPENTER algorithm, a data mining technique for discovering closed frequent itemsets from extremely long transactional databases by utilizing table transposition.

### Team Members
1. **Member 1**: [Name] - Data Preprocessing & Input Handling
2. **Member 2**: [Name] - CARPENTER Algorithm Core Implementation
3. **Member 3**: [Name] - Visualization & Analysis

---

## About CARPENTER Algorithm

CARPENTER (Closed pAttern mineR by transPositioN for ExTremely long pattERns) is an efficient algorithm for mining closed frequent itemsets, particularly useful when:
- The database is very long (many transactions)
- Patterns are short to medium length
- Memory efficiency is important

### Key Concepts:
- **Closed Patterns**: A pattern is closed if no superset has the same support
- **Table Transposition**: Converting row-based to column-based format for efficiency
- **Support**: Minimum frequency threshold for patterns to be considered

---

## Project Structure

```
CARPENTER_Project/
├── data/                    # Dataset storage
│   ├── raw/                 # Original datasets
│   └── processed/           # Preprocessed data
├── src/                     # Source code
│   ├── data_preprocessing.py    # Member 1
│   ├── carpenter_algorithm.py   # Member 2
│   └── visualization.py         # Member 3
├── notebooks/               # Jupyter notebooks
│   └── demo.ipynb          # Project demonstration
├── tests/                   # Unit tests
├── docs/                    # Documentation
├── results/                 # Output results and patterns
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

---

## Installation

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd CARPENTER_Project
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Task Division for Team Members

### 👤 Member 1: Data Preprocessing & Input Handling
**Responsibilities:**
- Load and parse transactional datasets
- Convert data to required format (transaction database)
- Data cleaning and validation
- Create sample datasets for testing
- Implement data statistics functions

**Files to work on:**
- `src/data_preprocessing.py`
- `data/` folder management
- Documentation on data format

**Deliverables:**
- Working data loader
- At least 2 sample datasets (small & medium)
- Data format documentation

---

### 👤 Member 2: CARPENTER Algorithm Core Implementation
**Responsibilities:**
- Implement table transposition logic
- Implement closed pattern mining algorithm
- Support counting and pattern validation
- Pattern closure checking
- Algorithm optimization

**Files to work on:**
- `src/carpenter_algorithm.py`
- Core algorithm logic

**Deliverables:**
- Complete CARPENTER implementation
- Pattern discovery functions
- Algorithm documentation with complexity analysis

---

### 👤 Member 3: Visualization & Analysis
**Responsibilities:**
- Visualize discovered patterns
- Performance metrics (runtime, memory)
- Create comparison charts
- Generate result reports
- Create interactive Jupyter notebook

**Files to work on:**
- `src/visualization.py`
- `notebooks/demo.ipynb`
- Results analysis

**Deliverables:**
- Pattern visualization functions
- Performance comparison charts
- Complete demo notebook
- Final presentation materials

---

## Timeline (Example for 4-week project)

### Week 1: Setup & Understanding
- All: Study CARPENTER algorithm
- Setup GitHub repository
- Initialize project structure
- Assign specific tasks

### Week 2: Individual Development
- Member 1: Complete data preprocessing
- Member 2: Start algorithm implementation
- Member 3: Setup visualization framework

### Week 3: Integration
- Integrate all modules
- Testing and debugging
- Member 2: Complete algorithm
- Member 3: Create visualizations

### Week 4: Finalization
- Complete demo notebook
- Documentation
- Testing with different datasets
- Prepare presentation

---

## Git Workflow

### Branch Strategy
```bash
main            # Stable, working code
├── dev         # Development branch
├── feature/data-preprocessing      # Member 1
├── feature/algorithm-core          # Member 2
└── feature/visualization           # Member 3
```

### Daily Workflow
1. Pull latest changes: `git pull origin dev`
2. Create/switch to your branch: `git checkout feature/your-feature`
3. Make changes and commit: `git add . && git commit -m "descriptive message"`
4. Push to GitHub: `git push origin feature/your-feature`
5. Create Pull Request to merge into `dev`

---

## Usage Example

```python
from src.data_preprocessing import load_dataset, preprocess_data
from src.carpenter_algorithm import CARPENTER
from src.visualization import plot_patterns, plot_performance

# Load data
transactions = load_dataset('data/raw/retail.txt')

# Run CARPENTER
minsup = 0.05  # 5% minimum support
carpenter = CARPENTER(minsup=minsup)
closed_patterns = carpenter.mine_patterns(transactions)

# Visualize results
plot_patterns(closed_patterns)
print(f"Found {len(closed_patterns)} closed patterns")
```

---

## Testing

Run tests:
```bash
python -m pytest tests/
```

---

## References

1. Pan, F., Cong, G., Tung, A. K., Yang, J., & Zaki, M. J. (2003). "CARPENTER: Finding Closed Patterns in Long Biological Datasets"
2. Frequent Pattern Mining - Data Mining Concepts
3. Closed Itemset Mining Algorithms

---

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request
5. Wait for code review

---

## License

This is an academic project for educational purposes.

---

## Contact

For questions or issues, contact team members or create an issue on GitHub.

---

**Last Updated**: December 2025
