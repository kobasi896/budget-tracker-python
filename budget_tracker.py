# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("expenses.csv")

# Print the raw data to verify it has been loaded correctly
print("\n--- Raw Data ---")
print(df)

# Calculate total spending
total_spent = df["Amount"].sum()
print("\n--- Total Spending ---")
print(f"£{total_spent:.2f}")

# Calculate spending by category
category_sum = df.groupby("Category")["Amount"].sum()
print("\n--- Spending by Category ---")
print(category_sum)

# Visualize spending by category using bar chart
category_sum.plot(kind="bar", title="Spending by Category")
plt.ylabel("Amount (£)")
plt.show()