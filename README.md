SMART EXPENSE TRACKER WITH ANALYTICS

Smart Expense Tracker with Analytics is a Python-based web application built using Streamlit. 
It helps users record daily expenses, analyze spending patterns through dashboards, maintain financial privacy,
calculate habit scores, detect recurring subscriptions, and predict future expenses using basic machine learning.

TECHNOLOGIES USED
Python
Streamlit (Frontend / GUI)
Pandas, NumPy (Data Processing)
Plotly, Matplotlib (Visualization)
Scikit-learn (Machine Learning)
CSV files (Data Storage)

FEATURES
Add and manage daily expenses
Category-wise and time-based analytics
Interactive charts and dashboards
Privacy mode to hide sensitive values
Habit score with badges
Subscription detection
Expense prediction using Linear Regression

PROJECT STRUCTURE
main.py
pages folder – add_expense.py, dashboard.py, analytics.py, settings.py
utils folder – db.py, insights.py, ml_model.py
data folder – expenses.csv, budgets.csv

HOW TO RUN
Install required libraries
Run the command: streamlit run main.py

LIMITATIONS
Uses CSV instead of database
Single-user system
ML prediction not shown in UI

FUTURE ENHANCEMENTS
Database integration
Mobile application
Advanced ML models
Budget alerts

AUTHOR
Semester 3 ETP Project
Smart Expense Tracker with Analytics
