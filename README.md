# Iris Dataset Analysis - README

## Overview
This Python script performs a comprehensive analysis of the classic Iris flower dataset, covering data loading, exploration, statistical analysis, and visualization using pandas, matplotlib, and seaborn.

## Features

### 1. Data Loading and Exploration
- Loads the Iris dataset from scikit-learn
- Creates a pandas DataFrame with proper column names
- Maps numeric species labels to human-readable names
- Provides:
  - First 5 rows preview
  - Dataset structure information
  - Missing values check

### 2. Statistical Analysis
- Computes basic statistics (mean, std, min/max, quartiles)
- Groups data by species and calculates mean values
- Identifies key findings about species characteristics

### 3. Data Visualization
Generates four complementary visualizations:
1. **Line chart**: Sepal length trend (by index)
2. **Bar chart**: Average petal length by species
3. **Histogram**: Distribution of sepal width
4. **Scatter plot**: Sepal vs petal length relationship

## Requirements
- Python 3.6+
- Required packages:
  ```bash
  pip install pandas matplotlib seaborn scikit-learn
  ```

## Usage
1. Save the script as `iris_analysis.py`
2. Run from command line:
   ```bash
   python iris_analysis.py
   ```

## Key Findings
- Setosa has significantly smaller petals than other species
- Virginica has the largest sepals on average
- Versicolor and virginica have similar sepal widths
- Clear correlation between sepal and petal lengths

## Output
The script produces:
1. Console output with:
   - Data preview
   - Statistical summaries
   - Key insights
2. A 2x2 grid of visualizations showing different aspects of the data

## Customization
To modify the analysis:
- Change figure sizes in `plt.figure(figsize=(15, 10))`
- Adjust histogram bins in `bins=15`
- Modify colors using seaborn palette options

## Troubleshooting
If you encounter errors:
1. Verify all packages are installed
2. Check Python version (3.6+ required)
3. Ensure you're using the correct Python environment

## License
This script is provided by David kamau. Feel free to modify(fork) and use in your projects.
