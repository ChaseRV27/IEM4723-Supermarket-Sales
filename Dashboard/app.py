
import streamlit as st

st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Supermarket Sales Analytics System")

st.subheader("ZAC Analysts | IEM 4723")

st.write(
    "Welcome to our supermarket sales analytics dashboard. "
    "This application will display sales statistics, "
    "charts, and business insights."
)

st.info("Dashboard development is currently in progress.")



import pandas as pd
from pathlib import Path

# Find the CSV file in the project's data folder
csv_path = Path(__file__).resolve().parent.parent / "data" / "SuperMarket Analysis.csv"

# Load the supermarket sales dataset
if csv_path.exists():
    df = pd.read_csv(csv_path)
    
    st.write("Actual CSV column names:", df.columns.tolist())

    st.header("Supermarket Sales Data")
    st.success("Dataset loaded successfully!")

# Interactive branch filter
    st.sidebar.header("Dashboard Filters")

    branch_options = ["All Branches"] + sorted(df["Branch"].unique().tolist())

    selected_branch = st.sidebar.selectbox(
        "Select Supermarket Branch",
        branch_options
    )

    if selected_branch == "All Branches":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["Branch"] == selected_branch]

        
    # Interactive product category filter
    product_options = ["All Products"] + sorted(df["Product line"].unique().tolist())

    selected_product = st.sidebar.selectbox(
        "Select Product Category",
        product_options
    )

    if selected_product != "All Products":
        filtered_df = filtered_df[
            filtered_df["Product line"] == selected_product
        ]



    # Calculate supermarket sales statistics
    total_sales = filtered_df["Sales"].sum()
    total_transactions = len(filtered_df)
    average_rating = filtered_df["Rating"].mean()
   

    # Display three dashboard metrics
    
    
    st.header("Sales Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Sales", f"${total_sales:,.2f}")

    with col2:
        st.metric("Total Transactions", f"{total_transactions:,}")

    with col3:
        st.metric("Average Customer Rating", f"{average_rating:.2f} / 10")

        
    # Calculate total sales by product category      
    sales_by_product = (
        filtered_df.groupby("Product line")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


    # Display sales chart
    st.header("Sales by Product Line")
    st.bar_chart(sales_by_product)

    
    # Sales trends over time
    st.header("Sales Over Time")

    # Convert transaction dates into actual dates
    sales_trend_df = filtered_df.copy()
    sales_trend_df["Date"] = pd.to_datetime(
        sales_trend_df["Date"]
    )

    # Calculate total sales for each day
    daily_sales = (
        sales_trend_df.groupby("Date")["Sales"]
        .sum()
        .sort_index()
    )

    # Display the sales trend
    st.line_chart(daily_sales)




    


    st.write("First 10 rows of the dataset:")
    st.dataframe(df.head(10))

    st.write(f"Total records: {len(df)}")
    st.write(f"Total columns: {len(df.columns)}")
else:
    st.error(f"Dataset not found: {csv_path}")

