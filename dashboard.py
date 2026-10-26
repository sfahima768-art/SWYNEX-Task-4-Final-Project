import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned student dataset
df = pd.read_csv("cleaned_student.csv")

# Convert Age and Marks to numeric values
for col in ["Age", "Marks"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Student Data Analytics Dashboard", fontsize=16)

# Total student records
axes[0, 0].bar(["Students"], [len(df)])
axes[0, 0].set_title("Total Student Records")
axes[0, 0].set_ylabel("Count")

# Age distribution
if "Age" in df.columns:
    df["Age"].dropna().hist(ax=axes[0, 1], bins=10)
    axes[0, 1].set_title("Age Distribution")
    axes[0, 1].set_xlabel("Age")
    axes[0, 1].set_ylabel("Frequency")

# Marks distribution
if "Marks" in df.columns:
    df["Marks"].dropna().hist(ax=axes[1, 0], bins=10)
    axes[1, 0].set_title("Marks Distribution")
    axes[1, 0].set_xlabel("Marks")
    axes[1, 0].set_ylabel("Frequency")

# Age vs Marks
if "Age" in df.columns and "Marks" in df.columns:
    axes[1, 1].scatter(df["Age"], df["Marks"])
    axes[1, 1].set_title("Age vs Marks")
    axes[1, 1].set_xlabel("Age")
    axes[1, 1].set_ylabel("Marks")

plt.tight_layout()
plt.savefig("student_dashboard.png", dpi=300)
plt.show()

print("Dashboard saved successfully!")