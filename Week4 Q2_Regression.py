import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("global_superstore_2016 Project.csv")

# Convert Sales and Profit to numeric
df["Sales"] = df["Sales"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

df["Profit"] = df["Profit"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# Features and target
X = df[["Quantity", "Discount", "Profit"]]
y = df["Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Q2 - Regression Model Results")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

# Actual vs Predicted
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()
