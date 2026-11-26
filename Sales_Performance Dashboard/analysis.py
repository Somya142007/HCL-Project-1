
import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(
    "dataset/cleaned_sales_data.csv",
    encoding="latin1"
)

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

print("\n========== SALES PERFORMANCE ANALYSIS ==========")

# 1. Total Sales
total_sales = df["Sales"].sum()

# 2. Total Profit
total_profit = df["Profit"].sum()

# 3. Total Orders
total_orders = df["Order ID"].nunique()

# 4. Total Quantity Sold
total_quantity = df["Quantity"].sum()

# 5. Average Order Value
average_order_value = total_sales / total_orders if total_orders else 0

# 6. Profit Margin
profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales else 0
)

print("\n----- Overall Business Performance -----")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Average Order Value:", round(average_order_value, 2))
print("Profit Margin:", round(profit_margin, 2), "%")

# 7. Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\n----- Category-wise Sales -----")
print(category_sales)

# 8. Region-wise Sales
region_sales = df.groupby("Region")["Sales"].sum()

print("\n----- Region-wise Sales -----")
print(region_sales)

# 9. Top 10 Products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n----- Top 10 Products -----")
print(top_products)

# 10. Monthly Sales
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n----- Monthly Sales -----")
print(monthly_sales)

print("\n========== ANALYSIS COMPLETED ==========")
