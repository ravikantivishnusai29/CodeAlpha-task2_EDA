import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("books_100_records.csv")

# ==========================
# Basic Dataset Information
# ==========================
print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== FIRST 5 RECORDS ==========")
print(df.head())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe(include='all'))

# ==========================
# Clean Price Column
# ==========================
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

# ==========================
# Graph 1 - Rating Distribution
# ==========================
plt.figure(figsize=(7,5))

df["Rating"].value_counts().sort_index().plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.savefig("rating_distribution.png")
plt.close()

print("✓ Rating Distribution Graph Saved")

# ==========================
# Graph 2 - Price Distribution
# ==========================
plt.figure(figsize=(7,5))

plt.hist(
    df["Price"],
    bins=10,
    color="orange",
    edgecolor="black"
)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.grid(alpha=0.5)

plt.savefig("price_distribution.png")
plt.close()

print("✓ Price Distribution Graph Saved")

# ==========================
# Save Cleaned Dataset
# ==========================
df.to_csv(
    "books_100_records_eda.csv",
    index=False,
    encoding="utf-8"
)

print("\n✓ Cleaned Dataset Saved Successfully")
print("✓ EDA Task Completed Successfully")