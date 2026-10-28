import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Online Shopping Analysis",
    page_icon="🛒",
    layout="wide"
)

# ShopAnalytics Website Styling
st.markdown("""

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap');

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #F1F3FA !important;
}

html, body, p, div, span, label, button, input {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif !important;
    color: #252B60 !important;
}

h1 {
    font-weight: 700 !important;
}

[data-testid="stSidebar"] {
    background-color: #EEF0FF;
    border-right: 1px solid #E0E4F5;
}


/* Dashboard Metric Cards */
[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #E5E9F5;
    box-shadow: 0 5px 15px rgba(60, 70, 130, 0.08);
}

/* First Card - Purple */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) [data-testid="stMetric"] {
    background: #EFEDFF;
    border-left: 5px solid #635BDB;
}

/* Second Card - Green */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) [data-testid="stMetric"] {
    background: #E5F8F0;
    border-left: 5px solid #159A76;
}

/* Third Card - Orange */
div[data-testid="stHorizontalBlock"] > div:nth-child(3) [data-testid="stMetric"] {
    background: #FFF3E2;
    border-left: 5px solid #D68A30;
}

/* Fourth Card - Pink */
div[data-testid="stHorizontalBlock"] > div:nth-child(4) [data-testid="stMetric"] {
    background: #FDEBF3;
    border-left: 5px solid #D96595;
}


[data-testid="stMetricValue"] {
    color: #5145CD;
    font-weight: 700;
}

[data-testid="stForm"] {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #E5E9F5;
}

.stButton button,
.stFormSubmitButton button,
.stDownloadButton button {
    background: #5B4FE9;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.stButton button:hover,
.stFormSubmitButton button:hover,
.stDownloadButton button:hover {
    background: #4338CA;
    color: white;
}

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* Welcome Banner */
.st-key-welcome_banner {
    background: linear-gradient(110deg, #E4E9FF, #D5E0FF);
    border-radius: 20px;
    padding: 25px 30px;
    margin-bottom: 20px;
    box-shadow: 0 5px 18px rgba(50, 60, 130, 0.08);
}

.st-key-welcome_banner h1 {
    color: #252B60;
}

.st-key-welcome_banner img {
    border-radius: 14px;
}
/* Website Fonts */
h1, h2, h3 {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)


# Sidebar Navigation

# Sidebar Navigation
with st.sidebar:
    st.title("🛍️ ShopAnalytics")
    st.caption("Shopping Analytics Dashboard")

    st.divider()

    
    
    menu = st.radio(
        "📌 Navigation",
        [
            "🏠 Dashboard",
            "➕ Add Transaction",
            "📊 Sales Analysis",
            "🏆 Product Analysis",
            "📦 View Transactions",
            "📥 Download Report"
        ],
        label_visibility="visible"
    )



    st.divider()
    st.caption("ShopAnalytics | Python Project")

    st.image(
        "images/shopanalytics_shopping_bags.png",
        use_container_width=True
    )



# Main Page Heading
if menu == "➕ Add Transaction":
    st.title("🛍️ ShopAnalytics")
    st.caption("Online Shopping Transaction Analysis System")
    st.write("Analyze orders, Revenue, Payments and Sales.")

# Read transactions from CSV file
df = pd.read_csv("transactions.csv")

# Add New Transaction
if menu == "➕ Add Transaction":
    st.header("➕ Add New Transaction")
    

    with st.form("transaction_form"):
        product = st.text_input("Product Name")
        quantity = st.number_input("Quantity", min_value=1, value=1)
        price = st.number_input("Price (₹)", min_value=0.01, value=100.0)
        payment = st.selectbox("Payment Method", ["UPI", "Card", "COD"])
        status = st.selectbox(
            "Order Status", ["Pending", "Delivered", "Cancelled"]
        )
        order_date = st.date_input("Order Date")
        submitted = st.form_submit_button("Save Transaction")

        if submitted:
            if not product.strip():
                st.error("Please enter a product name.")
            else:
                new_order = pd.DataFrame([{
                    "Order ID": int(df["Order ID"].max()) + 1,
                    "Date": str(order_date),
                    "Product": product.strip(),
                    "Quantity": quantity,
                    "Price": price,
                    "Payment": payment,
                    "Status": status
                }])

                new_order.to_csv(
                    "transactions.csv",
                    mode="a",
                    header=False,
                    index=False
                )

                st.success("Transaction saved successfully!")
                st.rerun()


# Calculate order values
df["Order Value"] = df["Quantity"] * df["Price"]
df["Date"] = pd.to_datetime(df["Date"])

# Dashboard

if menu == "🏠 Dashboard":
    with st.container(key="welcome_banner"):
        banner_left, banner_right = st.columns([3, 2])

        with banner_left:
            st.caption("WELCOME TO")
            st.title("ShopAnalytics")
            st.write(
                "Track orders, analyze transactions "
                "and explore sales insights."
            )

        with banner_right:
            st.image(
                "images/shopanalytics_shopping_bags.png",
                use_container_width=True
            )

    st.header("📊 Sales Dashboard")


    total_orders = len(df)

    total_revenue = df.loc[
        df["Status"] == "Delivered", "Order Value"
    ].sum()

    average_order = df["Order Value"].mean()
    delivered_orders = (df["Status"] == "Delivered").sum()

    col1, col2, col3, col4 = st.columns(4)

    
   
    col1.metric(
        "🛒 Total Orders",
        total_orders
    )

    col2.metric(
        "💰 Delivered Revenue",
        f"₹{total_revenue:,.0f}"
    )

    col3.metric(
        "📊 Avg Order Value",
        f"₹{average_order:,.0f}"
    )

    col4.metric(
        "📦 Delivered Orders",
        delivered_orders
    )

    st.header("📦 Transaction Records")
    st.dataframe(df, use_container_width=True)

    st.header("💳 Payment Method Analysis")

    payment_counts = df["Payment"].value_counts().reset_index()
    payment_counts.columns = ["Payment", "Orders"]

    fig1 = px.pie(
        payment_counts,
        names="Payment",
        values="Orders",
        title="Payment Method Distribution"
    )
    fig1.update_traces(
        marker=dict(colors=["#635BDB", "#159A76", "#F5A45D"])
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.header("🚚 Order Status Analysis")

    status_counts = df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Orders"]

    fig2 = px.bar(
        status_counts,
        x="Status",
        y="Orders",
        color="Status",
        title="Order Status Distribution"
    )
    fig2.update_traces(marker_line_width=0)
    fig2.for_each_trace(
        lambda trace: trace.update(
            marker_color={
                "Delivered": "#159A76",
                "Pending": "#F5A45D",
                "Cancelled": "#E879A5"
            }.get(trace.name, "#635BDB")
        )
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.header("📈 Daily Sales Analysis")

    daily_sales = df.groupby("Date", as_index=False)["Order Value"].sum()

    fig3 = px.line(
        daily_sales,
        x="Date",
        y="Order Value",
        markers=True,
        title="Daily Order Value"
    )
    fig3.update_traces(
    line=dict(color="#635BDB", width=3),
    fill="tozeroy",
    fillcolor="rgba(99, 91, 219, 0.15)"
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.success("Shopping Transaction Analysis Completed!")


    # Monthly Sales Analysis
    st.header("📅 Monthly Sales Analysis")

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    monthly_sales = df.groupby(
        "Month", as_index=False
    )["Order Value"].sum()

    fig4 = px.bar(
        monthly_sales,
        x="Month",
        y="Order Value",
        title="Monthly Order Value",
        color_discrete_sequence=["#635BDB"]
    )

    fig4.update_xaxes(type="category")

    st.plotly_chart(fig4, use_container_width=True)


    # Product-wise Sales Analysis
    st.header("🏆 Product Sales Analysis")

    product_sales = df.groupby(
        "Product", as_index=False
    )["Quantity"].sum()

    fig5 = px.bar(
        product_sales,
        x="Product",
        y="Quantity",
        title="Product-wise Units Sold"
    )

    fig5.update_traces(
        marker_color=[
            "#635BDB",
            "#39B98A",
            "#F5A45D",
            "#E879A5",
            "#7BA6E8",
            "#A78BFA",
            "#F4B860"
        ]
    )


    fig5.update_layout(
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(color="#252B60", family="Arial"),
        title_font=dict(size=18),
        margin=dict(l=25, r=25, t=65, b=25)
    )

    st.plotly_chart(fig5, use_container_width=True)


    # Download Transaction Report
    st.header("📥 Download Transaction Report")

    csv_data = df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        "Download CSV Report",
        data=csv_data,
        file_name="shopping_transaction_report.csv",
        mime="text/csv"
    )

# Separate Sales Analysis Page
if menu == "📊 Sales Analysis":
    st.header("📊 Sales Analysis")

    df["Order Value"] = df["Quantity"] * df["Price"]
    df["Date"] = pd.to_datetime(df["Date"])

    daily_sales = df.groupby(
        "Date", as_index=False
    )["Order Value"].sum()

    st.subheader("📈 Daily Sales")

    daily_chart = px.line(
        daily_sales,
        x="Date",
        y="Order Value",
        markers=True,
        title="Daily Order Value",
        color_discrete_sequence=["#635BDB"]
    )

    st.plotly_chart(daily_chart, use_container_width=True)

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    monthly_sales = df.groupby(
        "Month", as_index=False
    )["Order Value"].sum()

    st.subheader("📅 Monthly Sales")

    monthly_chart = px.bar(
        monthly_sales,
        x="Month",
        y="Order Value",
        title="Monthly Order Value",
        color_discrete_sequence=["#159A76"]
    )

    monthly_chart.update_xaxes(type="category")

    st.plotly_chart(monthly_chart, use_container_width=True)


# Product Analysis Page
if menu == "🏆 Product Analysis":
    st.header("🏆 Product Analysis")

    product_sales = df.groupby(
        "Product", as_index=False
    )["Quantity"].sum()

    fig_product = px.bar(
        product_sales,
        x="Product",
        y="Quantity",
        color="Product",
        title="Product-wise Units Sold",
        color_discrete_sequence=[
            "#635BDB",
            "#159A76",
            "#F5A45D",
            "#E879A5",
            "#7CA6E8"
        ]
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )

# View Transactions Page
if menu == "📦 View Transactions":
    st.header("📦 Transaction Records")

    records = df.copy()
    records["Order Value"] = records["Quantity"] * records["Price"]

    st.write("View all shopping transactions below.")

    st.dataframe(
        records,
        use_container_width=True,
        hide_index=True
    )

    st.metric("Total Transactions", len(records))

# Download Report Page
if menu == "📥 Download Report":
    st.header("📥 Download Transaction Report")

    st.write(
        "Download the complete shopping transaction "
        "data as a CSV file."
    )

    report_df = df.copy()

    report_df["Order Value"] = (
        report_df["Quantity"] * report_df["Price"]
    )

    report_df["Date"] = pd.to_datetime(
        report_df["Date"]
    ).dt.strftime("%Y-%m-%d")

    csv_data = report_df.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        label="📥 Download CSV Report",
        data=csv_data,
        file_name="ShopAnalytics_Transaction_Report.csv",
        mime="text/csv"
    )

    st.success("Your transaction report is ready!")
