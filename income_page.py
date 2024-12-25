from tkinter import *
import pandas as pd
import os

def go_to_income_page(root):
    def add_income():
        try:
            income_amount = entry_income.get()
            if income_amount:
                income_amount = float(income_amount)
                income_data = pd.DataFrame({
                    "income": [income_amount]
                })

                if os.path.exists("income.csv"):
                    income_data.to_csv("income.csv", mode="a", index=False, header=False)
                else:
                    income_data.to_csv("income.csv", mode="w", index=False, header=True)

                income_output.config(
                    text=f"Income added successfully: ₹{income_amount:.2f}",
                    fg="#006400"
                )
            else:
                income_output.config(text="Please enter an income amount.", fg="#8B0000")
        except ValueError:
            income_output.config(text="Invalid income! Please enter a number.", fg="#8B0000")

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#f0f0f0")

    Label(
        root,
        text="Income Page",
        font=("Helvetica", 20, "bold"),
        fg="#000080",
        bg="#f0f0f0"
    ).pack(pady=30)

    Label(
        root,
        text="Enter Monthly Income:",
        font=("Helvetica", 16),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=15)

    entry_income = Entry(root, width=40, font=("Helvetica", 14))
    entry_income.pack(pady=10)

    Button(
        root,
        text="Add Income",
        command=add_income,
        fg="white",
        bg="#004080",
        font=("Helvetica", 14, "bold"),
        width=12,
        height=1,
        relief="raised",
        bd=4
    ).pack(pady=25)

    global income_output
    income_output = Label(
        root,
        text="",
        font=("Helvetica", 14),
        fg="#8B0000",
        bg="#f0f0f0"
    )
    income_output.pack()
