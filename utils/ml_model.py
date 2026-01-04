import pandas as pd
from sklearn.linear_model import LinearRegression
def train_and_predict(df):
    if df.empty:
        return None
    df["Date"] = pd.to_datetime(df["Date"])
    monthly = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum().reset_index()
    monthly["Month"] = monthly["Date"].astype(str)
    monthly["Index"] = range(len(monthly))
    X = monthly[["Index"]]
    y = monthly["Amount"]
    if len(X) < 3:
        return None
    model = LinearRegression()
    model.fit(X, y)
    next_month_index = len(monthly)
    predicted = model.predict([[next_month_index]])

    return round(predicted[0], 2)
