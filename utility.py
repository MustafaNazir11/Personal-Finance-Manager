import pandas as pd
import os
from datetime import datetime

categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]


def save_user(name, email, password):
    """Saves user data to a CSV file."""
    new_data = pd.DataFrame({
        "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
        "name": [name],
        "email": [email],
        "password": [password]
    })
    if os.path.exists("result.csv"):
        new_data.to_csv("result.csv", mode="a", index=False, header=False)
    else:
        new_data.to_csv("result.csv", mode="w", index=False, header=True)

def check_user(email, password):
    """Checks if the user exists in the CSV."""
    if os.path.exists("result.csv"):
        df = pd.read_csv("result.csv")
        user = df[(df["email"] == email) & (df["password"] == password)]
        if not user.empty:
            return user.iloc[0]["name"]
    return None

def save_transaction(username, category, amount):
    """Saves transaction data to a CSV file."""
    new_transaction = pd.DataFrame({
        "username": [username],
        "category": [category],
        "amount": [amount]
    })
    if os.path.exists("transaction.csv"):
        new_transaction.to_csv("transaction.csv", mode="a", index=False, header=False)
    else:
        new_transaction.to_csv("transaction.csv", mode="w", index=False, header=True)
