import pandas as pd
import os

FILE_PATH = "expenses.csv"

def load_data():
    if not os.path.exists(FILE_PATH):
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
    return pd.read_csv(FILE_PATH)

def save_data(df):
    df.to_csv(FILE_PATH, index=False)
