from tkinter import *
import pandas as pd
import os

def go_to_income_page(root):
    """Navigates to the income page."""
    def add_income():
        """Handles adding monthly income."""
        try:
            income_amount = entry_income.get()

            if income_amount:
                income_amount = float(income_amount)  # Convert the input to a float
                income_data = pd.DataFrame({
                    "income": [income_amount]
                })

                # Check if the income file exists, then append or create
                if os.path.exists("income.csv"):
                    income_data.to_csv("income.csv", mode="a", index=False, header=False)
                else:
                    income_data.to_csv("income.csv", mode="w", index=False, header=True)

                income_output.config(
                    text=f"Income added successfully: ₹{income_amount:.2f}", fg="green"
                )
            else:
                income_output.config(text="Please enter an income amount.", fg="red")
        except ValueError:
            income_output.config(text="Invalid income! Please enter a number.", fg="red")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Income Page", font=("Times New Roman", 18, "bold"), fg="blue").pack(pady=10)
    Label(root, text="Enter Monthly Income:", font=("Times New Roman", 12)).pack(pady=10)

    Label(root, text="Income Amount:").pack()
    global entry_income
    entry_income = Entry(root, width=50, font=("Times New Roman", 18))
    entry_income.pack()

    Button(root, text="Add Income", command=add_income, fg="white", bg="blue", font=("Times New Roman", 18)).pack(pady=20)

    global income_output
    income_output = Label(root, text="", font=("Times New Roman", 18))
    income_output.pack()
