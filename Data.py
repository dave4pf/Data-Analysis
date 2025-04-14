# 1.Data loading and exploration steps.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

try:
    # Load the Iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target
    iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    # Display first 5 rows (using print instead of display)
    print("First 5 rows of the dataset:")
    print(iris_df.head())
    
    # Explore dataset structure
    print("\nDataset information:")
    print(iris_df.info())
    
    # Check for missing values
    print("\nMissing values:")
    print(iris_df.isnull().sum())
    
    # Basic statistics
    print("\nBasic statistics for numerical columns:")
    print(iris_df.describe())
    
    # Group by species and compute mean
    print("\nMean values by species:")
    species_stats = iris_df.groupby('species').mean()
    print(species_stats)
    
    # Data Visualization
    plt.figure(figsize=(15, 10))
    
    # 1. Line chart
    plt.subplot(2, 2, 1)
    iris_df['sepal length (cm)'].plot(kind='line', title='Sepal Length Trend')
    plt.ylabel('Sepal Length (cm)')
    
    # 2. Bar chart
    plt.subplot(2, 2, 2)
    species_stats['petal length (cm)'].plot(kind='bar', title='Average Petal Length by Species')
    plt.ylabel('Petal Length (cm)')
    
    # 3. Histogram
    plt.subplot(2, 2, 3)
    iris_df['sepal width (cm)'].plot(kind='hist', title='Distribution of Sepal Width', bins=15)
    plt.xlabel('Sepal Width (cm)')
    
    # 4. Scatter plot
    plt.subplot(2, 2, 4)
    plt.scatter(iris_df['sepal length (cm)'], iris_df['petal length (cm)'], c=iris_df['species'].astype('category').cat.codes)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error: {e}")
    
    # 2.Basic data analysis results.
    
    # Compute basic statistics
print("\nBasic statistics for numerical columns:")
display(iris_df.describe())

# Group by species and compute mean of numerical columns
print("\nMean values by species:")
species_stats = iris_df.groupby('species').mean()
display(species_stats)

# Interesting findings
print("\nInteresting findings:")
print("- Setosa has significantly smaller petal dimensions than other species")
print("- Virginica has the largest sepal length on average")
print("- Versicolor and virginica have similar sepal widths")

# 3 Data Visualization

# Set style for better looking plots
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# 1. Line chart (using index as pseudo-time for demonstration)
plt.subplot(2, 2, 1)
iris_df['sepal length (cm)'].plot(kind='line', title='Sepal Length Trend (by index)')
plt.ylabel('Sepal Length (cm)')

# 2. Bar chart - average petal length by species
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='petal length (cm)', data=iris_df, estimator=mean)
plt.title('Average Petal Length by Species')
plt.ylabel('Petal Length (cm)')

# 3. Histogram - distribution of sepal width
plt.subplot(2, 2, 3)
sns.histplot(iris_df['sepal width (cm)'], bins=15, kde=True)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')

# 4. Scatter plot - sepal length vs petal length
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()