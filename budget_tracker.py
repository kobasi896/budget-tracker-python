# Step 3a: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 3b: Load CSV file
df = pd.read_csv("expenses.csv")

# Step 3c: Print the raw data (optional)
print("\n--- Raw Data ---")
print(df)

# Step 3d: Calculate total spending
total_spent = df["Amount"].sum()
print("\n--- Total Spending ---")
print(f"£{total_spent:.2f}")

# Step 3e: Calculate spending by category
category_sum = df.groupby("Category")["Amount"].sum()
print("\n--- Spending by Category ---")
print(category_sum)

# Step 3f: Visualize spending by category using bar chart
category_sum.plot(kind="bar", title="Spending by Category")
plt.ylabel("Amount (£)")
plt.show()