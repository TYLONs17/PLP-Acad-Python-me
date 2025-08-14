# atomic_data_intelligence.py - Shadow Garden Data Intelligence Protocol

# Importing necessary modules for our mission
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris # A classic intel dataset for this operation

print("--- Initiating Shadow Garden Data Intelligence Protocol ---")
print("Objective: Infiltrate, Analyze, and Visualize Data with Atomic Precision.")
print("---------------------------------------------------------------")

# --- Task 1: Load and Explore the Dataset ---
print("\n[Phase 1: Data Infiltration and Reconnaissance]")

# Choose a dataset in CSV format (using Iris dataset as per suggestion)
# Using a try-except block to simulate file reading error handling,
# although load_iris is built-in and won't throw FileNotFoundError.
# This demonstrates the robust error handling required for file operations.
try:
    print("📡 Attempting to load Iris dataset (classified as 'Flower Metrics')...")
    iris = load_iris()
    # Convert to pandas DataFrame for easier manipulation
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    # --- ATOMIC FIX: Clean and rename column headers for direct access ---
    # This line iterates through the column names, removes " (cm)" and replaces spaces with underscores.
    df.columns = [col.replace(' (cm)', '').replace(' ', '_') for col in df.columns]

    # Map numerical target to actual species names
    species_map = {i: name for i, name in enumerate(iris.target_names)}
    # --- ATOMIC FIX: Ensure correct species assignment for all rows ---
    # Assign the numerical target first, then map to string names
    df['species'] = iris.target
    df['species'] = df['species'].map(species_map)

    print("✅ Iris Dataset Loaded Successfully. Intel secured. ✅")

    # Display the first few rows of the dataset using .head()
    print("\n📦 First 5 Tactical Data Rows (.head()):")
    print(df.head())

    # Explore the structure of the dataset by checking data types and missing values
    print("\n🔍 Dataset Structure (.info()):")
    df.info()

    print("\n🔍 Missing Value Scan (.isnull().sum()):")
    print(df.isnull().sum())

    # Clean the dataset by either filling or dropping any missing values.
    # For the Iris dataset, there are typically no missing values,
    # but we'll demonstrate the protocol for robustness.
    print("\n🧹 Initiating Data Cleaning Protocol (Handling Missing Values)...")
    if df.isnull().sum().sum() > 0:
        # Strategy: Drop rows with any missing values (atomic precision requires clean data)
        initial_rows = df.shape[0]
        df.dropna(inplace=True)
        cleaned_rows = df.shape[0]
        print(f"Report: Dropped {initial_rows - cleaned_rows} rows with missing intel.")
        print("✅ Data Cleaning Complete. Dataset is now pristine. ✅")
    else:
        print("Report: No missing intel detected. Dataset is already pristine.")
        print("✅ Data Cleaning Protocol bypassed as unnecessary. ✅")

except FileNotFoundError:
    print("\n🚨 ERROR: Specified intel file not found. Ensure path is correct. 🚨")
    print("Protocol halted. Cannot proceed without target data.")
    exit() # Exit the program if the file isn't found
except Exception as e:
    print(f"\n🚨 CRITICAL ERROR during data infiltration: {e}. Protocol Halted. 🚨")
    exit()

print("---------------------------------------------------------------")

# --- Task 2: Basic Data Analysis ---
print("\n[Phase 2: Tactical Data Analysis]")

# Compute the basic statistics of the numerical columns using .describe().
print("\n📊 Core Metrics Overview (.describe()):")
print(df.describe())

# Perform groupings on a categorical column ('species') and compute the mean of numerical columns for each group.
print("\n🧬 Species-Specific Mean Metrics (Grouped Analysis):")
# Identify numerical columns for grouping
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
grouped_means = df.groupby('species')[numerical_cols].mean()
print(grouped_means)

# Identify any patterns or interesting findings from your analysis.
print("\n🔭 Strategic Findings from Analysis:")
print("- **Iris Setosa (🌌Stealth-Type🌌):** Appears to have significantly smaller petal lengths and widths compared to others, indicating a distinct operational profile.")
print("- **Iris Versicolor (🌿Balance-Type🌿):** Shows intermediate values across all features, suggesting a versatile operational capability.")
print("- **Iris Virginica (✨Atomic-Type✨):** Exhibits the largest sepal and petal dimensions, indicating high-impact operational potential.")
print("- **Sepal Length vs. Petal Length:** There seems to be a positive correlation, where longer sepals generally accompany longer petals. This suggests a proportional development in these critical flower components.")
print("These insights will guide future strategic deployments.")
print("---------------------------------------------------------------")

# --- Task 3: Data Visualization ---
print("\n[Phase 3: Visual Intel Projection]")

# Setting a dark, atomic-themed style for plots
sns.set_style("darkgrid")
plt.rcParams.update({
    "figure.facecolor": "#1a202c",
    "axes.facecolor": "#2d3748",
    "text.color": "#e2e8f0",
    "axes.labelcolor": "#a0aec0",
    "xtick.color": "#a0aec0",
    "ytick.color": "#a0aec0",
    "grid.color": "#4a5568",
    "axes.edgecolor": "#805ad5",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.family": "Inter",
    "legend.edgecolor": "#5a6a7c"
})

# Create at least four different types of visualizations:

# 1. Bar chart showing the comparison of a numerical value across categories
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal_length', data=df, palette='viridis')
plt.title('Average Petal Length by Species (Tactical Comparison) 📊', fontsize=16, color='#c3a6ff')
plt.xlabel('Species Designation', fontsize=12)
plt.ylabel('Average Petal Length (mm)', fontsize=12)
plt.legend(title='Species')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
print("📊 Bar Chart: Average Petal Length by Species - Operational comparison projected. 📊")


# 2. Histogram of a numerical column to understand its distribution.
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_width'], bins=15, kde=True, color='#a78bfa')
plt.title('Distribution of Sepal Width (Component Fluctuation Analysis) 📈', fontsize=16, color='#c3a6ff')
plt.xlabel('Sepal Width (mm)', fontsize=12)
plt.ylabel('Frequency of Occurrence', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
print("📈 Histogram: Sepal Width Distribution - Component stability assessed. 📈")


# 3. Scatter plot to visualize the relationship between two numerical columns
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='magma', s=100, alpha=0.8)
plt.title('Sepal Length vs. Petal Length by Species (Inter-Component Relations) 🧬', fontsize=16, color='#c3a6ff')
plt.xlabel('Sepal Length (mm)', fontsize=12)
plt.ylabel('Petal Length (mm)', fontsize=12)
plt.legend(title='Species Designation')
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
print("🧬 Scatter Plot: Sepal vs. Petal Length - Relationship dynamics mapped. 🧬")


# 4. Line chart showing trends over time (adapted for categorical progression)
# We'll show the mean of each feature across species as a "trend" of characteristics.
plt.figure(figsize=(12, 7))
grouped_means.T.plot(kind='line', marker='o', figsize=(12, 7), colormap='plasma')
plt.title('Mean Feature Values Across Species (Evolutionary Trajectory) �', fontsize=16, color='#c3a6ff')
plt.xlabel('Feature', fontsize=12)
plt.ylabel('Mean Value (mm)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Species Designation', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
print("📉 Line Chart: Mean Feature Values Across Species - Evolutionary trends observed. 📉")

print("\n--- Data Intelligence Protocol Concluded. Insights secured. 🌙 ---")
�
