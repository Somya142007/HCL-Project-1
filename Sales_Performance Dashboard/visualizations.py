
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv(
    "dataset/cleaned_sales_data.csv",
    encoding="latin1"
)

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Set visualization style
sns.set_style("whitegrid")


# ==================================
# 1. MONTHLY SALES TREND
# ==================================

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()


# ==================================
# 2. CATEGORY-WISE SALES
# ==================================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(9, 6))
sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Category-wise Sales", fontsize=16)
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()


# ==================================
# 3. REGION-WISE SALES
# ==================================

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 8))

plt.pie(
    region_sales.values,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Region-wise Sales Distribution")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()


# ==================================
# 4. TOP 10 PRODUCTS
# ==================================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 7))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 10 Products by Sales", fontsize=16)
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()


print("All visualizations created successfully!")
