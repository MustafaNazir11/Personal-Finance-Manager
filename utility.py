import pandas as pd
import os
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]

def save_user(name, email, password):
    """Saves user data to a CSV file."""
    try:
        new_data = pd.DataFrame({
            "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
            "name": [name],
            "email": [email],
            "password": [password]  # Consider hashing passwords for security
        })

        if os.path.exists("register.csv"):
            new_data.to_csv("register.csv", mode="a", index=False, header=False)
        else:
            new_data.to_csv("register.csv", mode="w", index=False, header=True)

        logging.info(f"User '{email}' registered successfully.")
    except Exception as e:
        logging.error(f"Failed to save user '{email}': {e}")
        raise RuntimeError("Error saving user data.") from e

def check_user(email, password):
    """Checks if the user exists in the CSV."""
    try:
        if os.path.exists("register.csv"):
            df = pd.read_csv("register.csv")
            user = df[(df["email"] == email) & (df["password"] == password)]
            if not user.empty:
                logging.info(f"User '{email}' authenticated successfully.")
                return user.iloc[0]["name"]
        logging.warning(f"Authentication failed for email: {email}")
        return None
    except Exception as e:
        logging.error(f"Error checking user '{email}': {e}")
        raise RuntimeError("Error checking user data.") from e

def save_transaction(username, category, amount):
    """Saves transaction data to a CSV file."""
    try:
        if category not in categories:
            raise ValueError(f"Invalid category '{category}'. Must be one of {categories}.")

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        new_transaction = pd.DataFrame({
            "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
            "username": [username],
            "category": [category],
            "amount": [amount]
        })

        if os.path.exists("transaction.csv"):
            new_transaction.to_csv("transaction.csv", mode="a", index=False, header=False)
        else:
            new_transaction.to_csv("transaction.csv", mode="w", index=False, header=True)

        logging.info(f"Transaction for '{username}' saved successfully: {category} - ₹{amount:.2f}")
    except Exception as e:
        logging.error(f"Failed to save transaction for '{username}': {e}")
        raise RuntimeError("Error saving transaction data.") from e
