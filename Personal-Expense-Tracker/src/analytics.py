import pandas as pd
from src.database import connect_db

def show_monthly_summary():
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No expenses recorded yet.")
        return

    df["date"] = pd.to_datetime(df["date"])
    summary = df.groupby(df["date"].dt.month)["amount"].sum()
    print("\nMonthly Expense Summary:")
    print(summary)


def category_summary():
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    if df.empty:
        print("No expenses recorded yet.")
        return

    summary = df.groupby("category")["amount"].sum()
    print("\nCategory-wise Expense Summary:")
    print(summary)
