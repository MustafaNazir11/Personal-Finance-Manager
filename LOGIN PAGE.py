import tkinter as tk
from tkinter import messagebox
import pandas as pd


file = pd.read_csv("result.csv",usecols = ["email","password"],skipinitialspace=True)

email_list = file["email"].to_list()
password_list = file["password"].to_list()

email_password = dict(zip(email_list,password_list))



def login():
    email = email_entry.get()
    password = password_entry.get()
    if email in email_list and password == email_password[email]:
        messagebox.showinfo("Login Successful", "LOGED IN!")
    else:
        messagebox.showerror("Login Failed", "INVALID email OR PASSWORD! TRY AGAIN!")

def cancel():
    root.destroy()

root = tk.Tk()
root.title("FINANCE MANAGER LOGIN PAGE")
root.geometry("600x600")
root.configure(bg="black")

header = tk.Label(root, text="WELCOME TO LOGIN PAGE", font=("ITALIC",20, "bold"), fg="blue", bg="black")
header.pack(pady=100)

frame = tk.Frame(root, bg="black")
frame.pack(pady=50)

email_label = tk.Label(frame, text="Email:", bg="black", fg="white", font=("Arial", 12))
email_label.grid(row=0, column=0, padx=10, pady=10)

email_entry = tk.Entry(frame,font=("Arial", 12))
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(frame, text="Password:", bg="black", fg="white", font=("Arial", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(frame, text="Login", command=login, bg="green", fg="white", font=("Arial", 12))
login_button.grid(row=2,column=0,pady=20,padx=10)

cancel_button = tk.Button(frame, text="Cancel", command=cancel, bg="red", fg="white", font=("Arial", 12))
cancel_button.grid(row=2,column=1,pady=20,padx=10)

root.mainloop()

print(email_password)