from tkinter import *
from utility import check_user, navigate_to, centerWin
from transaction_page import transaction_page

def handle_login_success(root, username):
    for widget in root.winfo_children():
        widget.destroy()

    def logout():
        from Main import main_page  # Import here to avoid circular dependency
        navigate_to(root, main_page)

    root.configure(bg="#f0f0f0")

    Label(root, text=f"Welcome, {username}!", font=("Helvetica", 20, "bold"), fg="#000080", bg="#f0f0f0").pack(pady=30)

    Label(root, text="Choose an action:", font=("Helvetica", 16), fg="#404040", bg="#f0f0f0").pack(pady=15)

    Button(
        root,
        text="Transaction Page",
        command=lambda: transaction_page(root, username),
        fg="white",
        bg="#004080",
        font=("Helvetica", 14, "bold"),
        width=18,
        height=2,
        relief="raised",
        bd=4
    ).pack(pady=20)

    Button(
        root,
        text="Logout",
        command=logout,
        fg="white",
        bg="#004080",
        font=("Helvetica", 14, "bold"),
        width=18,
        height=2,
        relief="raised",
        bd=4
    ).pack(pady=20)

def login(root, home_page):
    def handle_login():
        user_email = entry_email.get()
        user_password = entry_password.get()
        username = check_user(user_email, user_password)
        if username:
            handle_login_success(root, username)
        else:
            label_output.config(text="Invalid email or password.", fg="#8B0000")

    for widget in root.winfo_children():
        widget.destroy()

    centerWin(root, 500, 500)
    root.configure(bg="#f0f0f0")

    Label(
        root,
        text="Login",
        font=("Helvetica", 22, "bold"),
        fg="#000080",
        bg="#f0f0f0"
    ).pack(pady=30)

    Label(
        root,
        text="Email:",
        font=("Helvetica", 14),
        bg="#f0f0f0"
    ).pack(pady=10)
    entry_email = Entry(root, width=40, font=("Helvetica", 14))
    entry_email.pack()

    Label(
        root,
        text="Password:",
        font=("Helvetica", 14),
        bg="#f0f0f0"
    ).pack(pady=10)
    entry_password = Entry(root, width=40, show="*", font=("Helvetica", 14))
    entry_password.pack()

    Button(
        root,
        text="Login",
        command=handle_login,
        fg="white",
        bg="#004080",
        font=("Helvetica", 14, "bold"),
        width=12,
        height=1,
        relief="raised",
        bd=4
    ).pack(pady=25)

    global label_output
    label_output = Label(
        root,
        text="",
        fg="#8B0000",
        font=("Helvetica", 14),
        bg="#f0f0f0"
    )
    label_output.pack()

    Button(root, text="Back", command=lambda: navigate_to(root, home_page), fg="white", bg="#808080",
           font=("Helvetica", 12, "bold"), width=10, height=1, relief="raised", bd=3).pack(pady=15)
