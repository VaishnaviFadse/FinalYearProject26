
import pandas as pd

# Load Orders data
df = pd.read_csv("global_superstore_2016 Project.csv")

# Q1
print("First 5 rows:")
print(df.head())

print("Basic information:")
print(df.info())

print("Shape:")
print(df.shape)

print("Columns:")
print(df.columns)


# Q2 - Missing values
print("Missing values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Check duplicates
print("Duplicate rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("Duplicates after removal:")
print(df.duplicated().sum())


# Q3 - Category-wise Total Sales

category_sales = df.groupby("Category")["Sales"].sum()

print("Total Sales by Category:")
print(category_sales)


# Q4 - Sort by multiple columns

sorted_df = df.sort_values(
    by=["Category", "Sales"],
    ascending=[True, False]
)

print("Sorted data:")
print(sorted_df)


# Q5 - Correlation Matrix

correlation = df.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation)
