import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
privacy_mode = st.sidebar.checkbox("Enable Privacy Mode", value=False)
DATA_PATH = "data/expense.csv"
st.title(" Expense Dashboard")
st.write("Visual breakdown of your spending habits ")
if not os.path.exists(DATA_PATH):
    st.warning("No expenses found. Add some entries first!")
    st.stop()
df = pd.read_csv(DATA_PATH)
if df.empty:
    st.warning("No expenses available. Add an expense first!")
    st.stop()
df["Date"] = pd.to_datetime(df["Date"])
st.sidebar.header("Filters")
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=list(range(1, 13)),
    index=datetime.now().month - 1
)
filtered_df = df[df["Date"].dt.month == selected_month]
if filtered_df.empty:
    st.info("No data for this month.")
    st.stop()
total = filtered_df["Amount"].sum()
top_category = filtered_df.groupby("Category")["Amount"].sum().idxmax()
top_day = filtered_df.groupby(filtered_df["Date"].dt.day)["Amount"].sum().idxmax()
c1, c2, c3 = st.columns(3)
def safe_value(value):
    if privacy_mode:
        return "₹ ****"
    return f"₹ {value:.2f}"
c1.metric("Total Spend", safe_value(total))
if privacy_mode:
    c2.metric("Top Category", "Hidden")
else:
    c2.metric("Top Category", top_category)
if privacy_mode:
    c3.metric("Highest Spending Day", "Hidden")
else:
    c3.metric("Highest Spending Day", top_day)

st.subheader(" Category Distribution")
pie_fig = px.pie(filtered_df, values="Amount", names="Category")
st.plotly_chart(pie_fig, use_container_width=True)
st.subheader(" Daily Spending Trend")
daily = filtered_df.groupby(filtered_df["Date"].dt.day)["Amount"].sum()
line_fig = px.line(
    x=daily.index,
    y=daily.values,
    markers=True,
    labels={"x": "Day of Month", "y": "Amount Spent"},
    title="Daily Spending Trend"
)
st.plotly_chart(line_fig, use_container_width=True)
st.subheader("Top 5 Largest Expenses This Month")
top5 = filtered_df.sort_values(by="Amount", ascending=False).head(5)
st.table(top5)
