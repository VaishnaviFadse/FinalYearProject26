import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Q1 - Load CSV
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("Dataset information:")
print(df.info())


# Q2 - Handle missing values
print("Missing values:")
print(df.isnull().sum())

df["Calories"] = df["Calories"].fillna(df["Calories"].mean())

df["Date"] = df["Date"].ffill()


print("Missing values after handling:")
print(df.isnull().sum())


# Q3 - Filter rows
high_pulse = df[df["Pulse"] > 100]

print("Pulse greater than 100:")
print(high_pulse)


# Q4 - Create new column
df["Calories_per_Minute"] = df["Calories"] / df["Duration"]

print("Data with new column:")
print(df.head())


# Q5 - Matplotlib visualization
plt.plot(df["Duration"], df["Calories"])

plt.xlabel("Duration")
plt.ylabel("Calories")
plt.title("Duration vs Calories")

plt.show()


# Q6 - Seaborn visualization
sns.scatterplot(
    data=df,
    x="Pulse",
    y="Calories"
)

plt.title("Pulse vs Calories")
plt.show()
