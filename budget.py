from src.database import connect_db

import pandas as pd

def check_budget(category, limit):
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    total = df[df["category"] == category]["amount"].sum()

    if total > limit:
        print(f" Budget exceeded for {category}! Spent: {total}")
    else:
        print(f" Budget OK for {category}. Spent: {total}")
