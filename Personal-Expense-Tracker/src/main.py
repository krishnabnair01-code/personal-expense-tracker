from src.database import create_table, connect_db
from src.analytics import show_monthly_summary, category_summary
from src.budget import check_budget
from ai.rag import ask_ai


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    desc = input("Enter description: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses VALUES (NULL, ?, ?, ?, ?)",
        (amount, category, date, desc)
    )
    conn.commit()
    conn.close()
    print("Expense added successfully.")


def view_expenses():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    conn.close()

    print("\nAll Expenses:")
    for row in rows:
        print(row)


def menu():
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Category Summary")
    print("5. Check Budget")
    print("6. Exit")
    print("7. Ask AI about my expenses")


if __name__ == "__main__":
    create_table()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            cat = input("Enter category: ")
            limit = float(input("Enter budget limit: "))
            check_budget(cat, limit)
        elif choice == "6":
            print("Goodbye!")
        elif choice == "7":
            q = input("Ask your question: ")
            answer = ask_ai(q)
            print("\nAI Insight:")
            print(answer)
            break
        else:
            print("Invalid choice")

