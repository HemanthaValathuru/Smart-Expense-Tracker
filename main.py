import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
from utils.db import load_data
from utils.insights import (
    calculate_habit_score,
    get_badges,
)
st.set_page_config(
    page_title="Smart Expense Tracker",
    page_icon="💸",
    layout="wide"
)
st.title("💸 Smart Expense Tracker")
st.write("Your personalized financial dashboard ")
df = load_data()
if not df.empty:
    df["Date"] = pd.to_datetime(df["Date"])
st.sidebar.header("⚙ Settings")
st.subheader(" Summary")
st.subheader(" Category Breakdown")
st.subheader(" Habit Score")
if not df.empty:
    score = calculate_habit_score(df)
    badges = get_badges(score)

    st.metric("Your Score", f"{score}/100")

    st.write("Badges Earned:")
    st.write(" ".join(badges))
else:
    st.info("Your score will appear once you add expenses.")


