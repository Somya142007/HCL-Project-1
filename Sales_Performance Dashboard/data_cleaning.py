
import pandas as pd
import numpy as np

# 1. Load the original dataset
df = pd.read_csv(
    "dataset/sales_data.csv",
    encoding="latin1"
)

print("Original Dataset:")
print(df.head())

# 2. Check dataset information
print("\nDataset Information:")
print(df.info())

# 3. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Convert Order Date into datetime format
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

# 7. Remove records with missing essential values
df = df.dropna(
    subset=["Order ID", "Order Date", "Sales"]
)

# 8. Save cleaned dataset
df.to_csv("dataset/cleaned_sales_data.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned Dataset Shape:", df.shape)
