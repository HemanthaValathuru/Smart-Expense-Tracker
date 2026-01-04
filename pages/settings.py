import streamlit as st
import pandas as pd
import os
from utils.insights import calculate_habit_score, get_badges
DATA_PATH = "data/expense.csv"
st.title(" Settings & Preferences")
st.write("Customize your finance experience ")
if not os.path.exists(DATA_PATH):
    st.warning("No expenses found yet!")
    st.stop()
df = pd.read_csv(DATA_PATH)
st.subheader(" Habit Score & Badges")
if df.empty:
    st.info("Add some expenses to see your score.")
else:
    score = calculate_habit_score(df)
    st.metric("Your Habit Score", f"{score}/100")
    badges = get_badges(score)
    st.write("Your Badges:")
    st.write(" ".join(badges))
st.subheader(" Monthly Budget Settings")
categories = [
    "Food", "Shopping", "Subscriptions",
    "Groceries", "Health"
]
st.write("Set a recommended budget for each category:")
budget_values = {}
for cat in categories:
    budget = st.number_input(f"Budget for {cat} (₹)", min_value=0, value=2000)
    budget_values[cat] = budget
if st.button("Save Budgets"):
    budget_df = pd.DataFrame(list(budget_values.items()), columns=["Category", "Budget"])
    budget_df.to_csv("data/budgets.csv", index=False)
    st.success("Budgets saved successfully!")
