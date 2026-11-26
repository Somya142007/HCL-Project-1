
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(
        "dataset/cleaned_sales_data.csv",
        encoding="latin1"
    )
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# Dashboard heading
st.title("📊 Sales Performance Dashboard")
st.markdown("### Analyze sales, profit, products and regional performance")
st.divider()

# Sidebar filters
st.sidebar.header("Filter Sales Data")

regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].dropna().unique()),
    default=sorted(df["Region"].dropna().unique())
)

categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].dropna().unique()),
    default=sorted(df["Category"].dropna().unique())
)

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Apply filters
filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories))
]

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df["Order Date"].dt.date >= start_date) &
        (filtered_df["Order Date"].dt.date <= end_date)
    ]

if filtered_df.empty:
    st.warning("No sales data found for the selected filters.")
    st.stop()

# Calculate KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()

# Display metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Total Quantity", f"{total_quantity:,}")

st.divider()

# Monthly sales trend
st.subheader("📈 Monthly Sales Trend")

monthly_df = filtered_df.copy()
monthly_df["Month"] = monthly_df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
    monthly_df.groupby("Month", as_index=False)["Sales"].sum()
)

fig1 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# Category and region charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Category-wise Sales")

    category_sales = (
        filtered_df.groupby("Category", as_index=False)["Sales"].sum()
    )

    fig2 = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        color="Category",
        title="Sales by Category"
    )

    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("Region-wise Sales")

    region_sales = (
        filtered_df.groupby("Region", as_index=False)["Sales"].sum()
    )

    fig3 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Regional Sales Distribution"
    )

    st.plotly_chart(fig3, use_container_width=True)

# Top 10 products
st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

fig4 = px.bar(
    top_products.sort_values("Sales"),
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig4, use_container_width=True)

# Dataset preview
st.subheader("📋 Sales Data Preview")

st.dataframe(filtered_df, use_container_width=True)

st.success("Dashboard loaded successfully!")
