import pandas as pd
from datetime import datetime, timedelta


# PRIVACY FILTER

def privacy_filter(value, privacy_on):
    if privacy_on:
        return "₹ ****"
    return f"₹ {float(value):.2f}"



# HABIT SCORE

def calculate_habit_score(df):

    if df.empty:
        return 0

    df["Date"] = pd.to_datetime(df["Date"])

    # NO-SPEND DAYS
    all_days = pd.date_range(df["Date"].min(), df["Date"].max())
    spend_days = df["Date"].dt.date.unique()
    no_spend_days = len(all_days) - len(spend_days)
    no_spend_score = min(50, no_spend_days * 1.2)

    # CATEGORY BALANCE
    category_balance_score = 30 - df.groupby("Category")["Amount"].sum().max() * 0.02
    category_balance_score = max(5, min(50, category_balance_score))

    final_score = no_spend_score + category_balance_score
    final_score = int(max(10, min(100, final_score)))

    return final_score



# BADGES
def get_badges(score):
    badges = []

    if score >= 85:
        badges.append(" Budget Master")
    if score >= 70:
        badges.append(" Consistent Saver")
    if score >= 60:
        badges.append(" Steady Progress")
    if score >= 50:
        badges.append(" Controlled Spender")
    if score < 40:
        badges.append(" Needs Balance")

    return badges



# SUBSCRIPTION DETECTION

def detect_subscriptions(df):
    """
    Detects recurring monthly expenses (e.g. Netflix, Gym).
    """

    if df.empty:
        return pd.DataFrame()

    df["Date"] = pd.to_datetime(df["Date"])

    subscriptions = []

    for cat in df["Category"].unique():
        cat_data = df[df["Category"] == cat].sort_values("Date")

        if len(cat_data) < 3:
            continue

        # Check gaps between purchases
        diffs = cat_data["Date"].diff().dt.days.dropna()

        # Monthly gaps between 25–35 days
        recurring = (diffs.between(25, 35)).sum()

        if recurring >= 2:
            subscriptions.append({
                "Subscription": cat,
                "Occurrences": len(cat_data),
                "Average Amount": round(cat_data["Amount"].mean(), 2)
            })

    return pd.DataFrame(subscriptions)


