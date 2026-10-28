# 🛍️ ShopAnalytics
## Online Shopping Transaction Analysis System

### 📌 Project Overview
ShopAnalytics is a web-based application developed using Python and Streamlit. It helps analyze online shopping transactions, track orders, monitor revenue, and visualize sales performance through interactive dashboards.

### 🎯 Objectives
- Analyze online shopping transaction data.
- Calculate total orders and revenue.
- Track order status and payment methods.
- Identify product-wise sales performance.
- Display daily and monthly sales trends.

### ✨ Features
- **Dashboard:** Displays total orders, delivered revenue, average order value, and delivered orders.
- **Add Transaction:** Allows users to enter new shopping transactions.
- **Sales Analysis:** Visualizes daily and monthly sales trends.
- **Product Analysis:** Displays product-wise units sold.
- **View Transactions:** Shows transaction records in a table.
- **Download Report:** Allows users to download transaction data as a CSV file.

### 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- CSV
- GitHub

### 📂 Project Structure

```text
Online-Shopping-Transaction-Analysis-System/
│
├── app.py
├── transactions.csv
├── requirements.txt
└── images/
    └── shopanalytics_shopping_bags.png
```

### 🚀 How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/jyoshikapotnuru234-create/Online-Shopping-Transaction-Analysis-System.git
```

**2. Open the project folder**

```bash
cd Online-Shopping-Transaction-Analysis-System
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
streamlit run app.py
```

### 📊 Expected Outcome
An interactive shopping analytics dashboard that helps users understand transaction activity, sales trends, product performance, and payment preferences.

### 👥 Project Team
Developed as a team academic project.

### 📝 Note
The application uses a CSV file for storing transaction records. On Streamlit Community Cloud, newly added transactions may not persist after the app restarts.
