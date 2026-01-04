import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import calplot
from datetime import datetime
import os
DATA_PATH = "data/expense.csv"
st.title(" Analytics & Heatmap")
st.write("A deeper look into your spending patterns ")
if not os.path.exists(DATA_PATH):
    st.warning("No expenses found. Add entries first!")
    st.stop()
df = pd.read_csv(DATA_PATH)
if df.empty:
    st.info("No data available yet!")
    st.stop()
df["Date"] = pd.to_datetime(df["Date"])
st.subheader(" Heatmap Filters")
years = sorted(df["Date"].dt.year.unique())
selected_year = st.selectbox("Select Year", years)
df_year = df[df["Date"].dt.year == selected_year]
if df_year.empty:
    st.info("No data for this year.")
    st.stop()
st.subheader(" Expense Heatmap ")
heat_data = df_year.groupby("Date")["Amount"].sum()
fig, ax = calplot.calplot(
    heat_data,
    cmap="YlOrRd",
    suptitle=f"Expense Heatmap for {selected_year}"
)
st.pyplot(fig)
st.subheader(" Monthly Spending Trend")
monthly = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()
fig2, ax2 = plt.subplots()
ax2.plot(monthly.index.astype(str), monthly.values, marker="o")
ax2.set_xlabel("Month")
ax2.set_ylabel("Amount Spent")
ax2.set_title("Monthly Spending Trend")
st.pyplot(fig2)
st.subheader(" Spending Highlights")
daily = df.groupby(df["Date"].dt.date)["Amount"].sum()
col1, col2 = st.columns(2)
col1.metric("Highest Spend Day", f"{daily.idxmax()}", f"₹ {daily.max():.2f}")
col2.metric("Lowest Spend Day", f"{daily.idxmin()}", f"₹ {daily.min():.2f}")
