import os
from openai import OpenAI
from src.database import connect_db
from src.database import connect_db

def get_expense_text():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT amount, category, date, description FROM expenses")
    rows = cur.fetchall()
    conn.close()

    texts = []
    for r in rows:
        texts.append(
            f"On {r[2]}, spent {r[0]} rupees on {r[1]} for {r[3]}"
        )
    return texts
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question):
    expense_text = get_expense_text()

    context = "\n".join(expense_text)

    prompt = f"""
You are a financial analyst.
Here is the user's expense data:
{context}

Question:
{question}

Answer clearly with insights and suggestions.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
