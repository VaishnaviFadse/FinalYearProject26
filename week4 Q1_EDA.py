import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("global_superstore_2016 Project.csv")

# Convert Sales and Profit into numeric values
df["Sales"] = df["Sales"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

df["Profit"] = df["Profit"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Values
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical Analysis
print("\nStatistical Summary:")
print(df.describe())

# Total Sales And Profit
print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())


#Categoriwise Sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

# Region Wise Sales
region_sales = df.groupby("Region")["Sales"].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Sales Visuvalization Bar Charts
plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


#Profit Visuvalization
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8, 5))

region_profit.plot(kind="bar")

plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# Sales Vs.Profit
plt.figure(figsize=(8, 5))

sns.scatterplot(data=df, x="Sales", y="Profit")

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()


