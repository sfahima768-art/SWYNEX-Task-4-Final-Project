import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the cleaned dataset
df = pd.read_csv("cleaned student.csv")

# Display basic information
print("EXPLORATORY DATA ANALYSIS")
print("=" * 40)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Create output folder
os.makedirs("eda_outputs", exist_ok=True)

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# Create histograms
if not numeric_df.empty:
    numeric_df.hist(figsize=(10, 6))
    plt.tight_layout()
    plt.savefig("eda_outputs/histograms.png")
    plt.close()

# Create correlation heatmap
if len(numeric_df.columns) >= 2:
    correlation = numeric_df.corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(correlation, cmap="coolwarm", aspect="auto")
    plt.colorbar()
    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=45
    )
    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("eda_outputs/correlation_heatmap.png")
    plt.close()

# Create boxplots to identify outliers
for column in numeric_df.columns:
    plt.figure()
    plt.boxplot(numeric_df[column].dropna())
    plt.title(f"Boxplot of {column}")
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig(f"eda_outputs/{column}_boxplot.png")
    plt.close()

print("\nAnalysis completed!")
print("Charts saved in the eda_outputs folder.")