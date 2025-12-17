# GitHub Collaboration Guide for CARPENTER Project

## Initial Setup (Do this ONCE per team)

### Step 1: Create GitHub Repository

**One team member (Project Lead) should:**

1. Go to [GitHub](https://github.com) and sign in
2. Click "New Repository" (green button)
3. Repository settings:
   - Name: `CARPENTER_Project`
   - Description: "CARPENTER Algorithm: Closed Pattern Discovery by Transposing Tables"
   - Visibility: Public or Private (as per your preference)
   - ✅ Add a README file
   - ✅ Add .gitignore: Python
   - License: MIT (optional)
4. Click "Create Repository"
5. Copy the repository URL (e.g., `https://github.com/yourusername/CARPENTER_Project.git`)

### Step 2: Share Repository Access

**Project Lead should:**

1. Go to repository Settings → Collaborators
2. Click "Add people"
3. Add team members by GitHub username or email
4. Team members will receive invitation emails

---

## Each Team Member Setup (Do this ONCE per person)

### Step 1: Install Git

**Windows:**
```powershell
# Check if Git is installed
git --version

# If not installed, download from: https://git-scm.com/download/win
```

### Step 2: Configure Git

```powershell
# Set your name and email (use your GitHub email)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --global --list
```

### Step 3: Clone the Repository

```powershell
# Navigate to where you want the project (D drive)
cd D:\

# Clone the repository (replace with your actual repo URL)
git clone https://github.com/yourusername/CARPENTER_Project.git

# Navigate into the project
cd CARPENTER_Project

# Verify you're on the main branch
git branch
```

### Step 4: Create Your Feature Branch

Each team member works on their own branch:

```powershell
# Member 1 - Data Preprocessing
git checkout -b feature/data-preprocessing

# Member 2 - Algorithm Implementation
git checkout -b feature/algorithm-core

# Member 3 - Visualization
git checkout -b feature/visualization
```

---

## Daily Git Workflow

### Morning Routine (Before starting work)

```powershell
# 1. Switch to main branch
git checkout main

# 2. Get latest changes from GitHub
git pull origin main

# 3. Switch back to your feature branch
git checkout feature/your-feature-name

# 4. Merge latest changes from main into your branch
git merge main

# 5. Start coding!
```

### During Work (Save your progress)

```powershell
# 1. Check what files you've changed
git status

# 2. See detailed changes
git diff

# 3. Add files to staging area
git add .                           # Add all changes
# OR
git add src/data_preprocessing.py  # Add specific file

# 4. Commit your changes with a clear message
git commit -m "Implement data loading functionality"

# Good commit message examples:
# "Add load_dataset function with CSV support"
# "Fix bug in transaction preprocessing"
# "Update README with installation instructions"
# "Implement CARPENTER pattern closure checking"
```

### Evening Routine (Push your work to GitHub)

```powershell
# 1. Make sure all changes are committed
git status

# 2. Push your branch to GitHub
git push origin feature/your-feature-name

# If first time pushing this branch:
git push -u origin feature/your-feature-name
```

---

## Merging Your Work

### When Your Feature is Complete

**Option 1: Pull Request (Recommended)**

1. Go to GitHub repository in browser
2. You'll see "Compare & pull request" button - click it
3. Fill in pull request details:
   - Title: "Feature: Data Preprocessing Module"
   - Description: What you implemented, any issues, etc.
4. Request review from team members
5. Wait for approval
6. Click "Merge pull request"
7. Delete branch after merging

**Option 2: Direct Merge (For small teams)**

```powershell
# 1. Switch to main branch
git checkout main

# 2. Pull latest changes
git pull origin main

# 3. Merge your feature branch
git merge feature/your-feature-name

# 4. Push to GitHub
git push origin main

# 5. Delete local branch (optional)
git branch -d feature/your-feature-name
```

---

## Common Git Commands Cheat Sheet

```powershell
# === Status & Information ===
git status                    # See current changes
git log                       # View commit history
git log --oneline            # Compact commit history
git branch                   # List branches
git branch -a                # List all branches (including remote)

# === Getting Latest Code ===
git pull origin main         # Get latest from main branch
git fetch origin            # Download changes without merging

# === Making Changes ===
git add filename.py         # Stage specific file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes
git commit -am "message"    # Stage and commit all (tracked files only)

# === Branching ===
git checkout branch-name        # Switch to branch
git checkout -b new-branch     # Create and switch to new branch
git branch branch-name         # Create new branch
git branch -d branch-name      # Delete branch

# === Pushing & Pulling ===
git push origin branch-name    # Push branch to GitHub
git pull origin branch-name    # Pull branch from GitHub

# === Undoing Changes ===
git checkout -- filename.py    # Discard changes to file
git reset HEAD filename.py     # Unstage file
git reset --hard HEAD         # Discard ALL uncommitted changes (CAREFUL!)

# === Viewing Changes ===
git diff                      # See unstaged changes
git diff --staged            # See staged changes
git diff main feature/branch  # Compare branches
```

---

## Handling Merge Conflicts

If two people edit the same file, you might get conflicts:

```powershell
# 1. Try to merge or pull
git pull origin main

# If conflict occurs:
# CONFLICT (content): Merge conflict in src/data_preprocessing.py

# 2. Open the conflicting file in VS Code
# You'll see markers like:
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> main

# 3. Edit the file to keep what you want
# Remove the conflict markers

# 4. Stage the resolved file
git add src/data_preprocessing.py

# 5. Complete the merge
git commit -m "Resolve merge conflict in data_preprocessing"

# 6. Push
git push origin feature/your-feature-name
```

---

## Project Workflow Example

### Week 1: Setup & Initial Work

```powershell
# Member 1: Data Preprocessing
cd D:\CARPENTER_Project
git checkout -b feature/data-preprocessing
# ... do work on data_preprocessing.py ...
git add src/data_preprocessing.py
git commit -m "Implement DataLoader class with basic functions"
git push origin feature/data-preprocessing

# Member 2: Algorithm Core
git checkout -b feature/algorithm-core
# ... do work on carpenter_algorithm.py ...
git add src/carpenter_algorithm.py
git commit -m "Implement CARPENTER class skeleton"
git push origin feature/algorithm-core

# Member 3: Visualization
git checkout -b feature/visualization
# ... do work on visualization.py ...
git add src/visualization.py
git commit -m "Create PatternVisualizer class with plot functions"
git push origin feature/visualization
```

### Week 2: Integration

```powershell
# All members: Merge completed features to main
# Member 1 finishes first
git checkout main
git pull origin main
git merge feature/data-preprocessing
git push origin main

# Member 2 & 3: Update your branches with Member 1's code
git checkout feature/algorithm-core
git merge main
# Continue working with access to data_preprocessing.py
```

### Week 3: Testing & Documentation

```powershell
# All work together on main or create test branches
git checkout -b testing
# ... test integration ...
git commit -am "Add integration tests"
git checkout main
git merge testing
git push origin main
```

---

## Best Practices

### ✅ DO:
- Commit often (multiple times per day)
- Write clear commit messages
- Pull before you push
- Keep commits focused (one feature/fix per commit)
- Test before committing
- Communicate with team about major changes

### ❌ DON'T:
- Commit broken code to main
- Push without testing
- Make huge commits with many unrelated changes
- Work directly on main branch
- Forget to pull before starting work
- Use `git push --force` (unless you know what you're doing)

---

## Troubleshooting

### Problem: "Permission denied" when pushing
```powershell
# Solution: Check you're added as collaborator
# Or use HTTPS with personal access token
```

### Problem: "Your branch is behind"
```powershell
# Solution: Pull first
git pull origin main
git push origin main
```

### Problem: "Untracked files"
```powershell
# Solution: Add files or update .gitignore
git add .
# OR edit .gitignore to exclude them
```

### Problem: Accidentally committed to main
```powershell
# Solution: Move commit to feature branch
git branch feature/my-work      # Create branch with current commits
git reset --hard origin/main   # Reset main to match GitHub
git checkout feature/my-work   # Continue work here
```

---

## GitHub Desktop Alternative

If command line is difficult, use **GitHub Desktop**:

1. Download: https://desktop.github.com/
2. Sign in with GitHub account
3. Clone repository
4. Use GUI for commits, pushes, and pulls
5. Much easier for beginners!

---

## Team Communication

### During Collaboration:

1. **Create Issues** on GitHub for tasks
2. **Comment on Pull Requests** for code review
3. **Use Project Board** (GitHub Projects) to track progress
4. **Discuss** in repository Discussions tab

### Before Merging:

1. Review each other's code
2. Test integration together
3. Ensure all tests pass
4. Update documentation

---

## Final Submission Checklist

Before submitting your project:

```powershell
# 1. Ensure all work is merged to main
git checkout main
git pull origin main

# 2. Test the entire project
jupyter notebook notebooks/demo.ipynb

# 3. Update README with final details
git add README.md
git commit -m "Update README for submission"
git push origin main

# 4. Create a release tag
git tag -a v1.0 -m "Final submission version"
git push origin v1.0

# 5. Download repository as ZIP (backup)
# Go to GitHub → Code → Download ZIP
```

---

## Getting Help

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- Pro Git Book (free): https://git-scm.com/book/en/v2

---

**Happy Collaborating! 🚀**
