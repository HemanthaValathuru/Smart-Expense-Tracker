import streamlit as st
import pandas as pd
from datetime import datetime
import os
DATA_PATH = "data/expense.csv"
st.title("➕ Add New Expense")
if not os.path.exists(DATA_PATH):
    df = pd.DataFrame(columns=["Date", "Amount", "Category", "Note"])
    df.to_csv(DATA_PATH, index=False)
with st.form("expense_form"):
    date = st.date_input("Date", datetime.now())
    amount = st.number_input("Amount (₹)", min_value=1.0, format="%.2f")
    category = st.selectbox("Category", [
        "Food", "Shopping", "Travel", "Bills", "Subscriptions",
        "Groceries", "Entertainment", "Health", "Others"
    ])
    note = st.text_input("Note (optional)")
    receipt = st.file_uploader("Upload Receipt (optional)", type=["jpg", "png", "jpeg"])
    submitted = st.form_submit_button("Add Expense")
if submitted:
    new_data = pd.DataFrame(
        [[date, amount, category, note]],
        columns=["Date", "Amount", "Category", "Note"]
    )
    df = pd.read_csv(DATA_PATH)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
    st.success("Expense added successfully!")
    if receipt:
        folder = "data/receipts"
        os.makedirs(folder, exist_ok=True)
        receipt_path = os.path.join(folder, receipt.name)
        with open(receipt_path, "wb") as f:
            f.write(receipt.getbuffer())
        st.info(f"Receipt saved at {receipt_path}")
