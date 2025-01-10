from tkinter import *
from register import register
from login import login
from about_page import about_page
from utility import centerWin
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


def on_hover(button, color):
    """Changes button color on hover."""
    button.bind("<Enter>", lambda e: button.config(bg=color))
    button.bind("<Leave>", lambda e: button.config(bg=button.default_bg))


def main_page(root):
    """
    Sets up the homepage with enhanced aesthetics and user experience.
    """
    for widget in root.winfo_children():
        widget.destroy()

    # Window configuration
    root.title("Personal Finance Manager")
    root.configure(bg="#e8f0f7")

    # Header with optional logo
    header_frame = Frame(root, bg="#e8f0f7")
    header_frame.pack(pady=30)

    Label(
        header_frame,
        text="💰",
        font=("Arial", 40),
        bg="#e8f0f7"
    ).pack()

    Label(
        header_frame,
        text="PERSONAL FINANCE MANAGER",
        font=("Arial", 28, "bold"),
        fg="#003366",
        bg="#e8f0f7"
    ).pack()

    Label(
        header_frame,
        text="Manage your finances efficiently and effortlessly",
        font=("Arial", 14, "italic"),
        fg="#555555",
        bg="#e8f0f7"
    ).pack(pady=5)

    # Buttons
    button_frame = Frame(root, bg="#e8f0f7")
    button_frame.pack(pady=20)

    button_style = {
        "font": ("Arial", 14, "bold"),
        "width": 20,
        "height": 2,
        "relief": "flat",
        "bd": 0,
        "cursor": "hand2"
    }

    btn_register = Button(
        button_frame,
        text="Register",
        command=lambda: register(root, main_page),
        fg="white",
        bg="#0078d7",
        activebackground="#005bb5",
        activeforeground="white",
        **button_style
    )
    btn_register.default_bg = "#0078d7"
    btn_register.pack(pady=10)
    on_hover(btn_register, "#005bb5")

    btn_login = Button(
        button_frame,
        text="Login",
        command=lambda: login(root, main_page),
        fg="white",
        bg="#28a745",
        activebackground="#1e7e34",
        activeforeground="white",
        **button_style
    )
    btn_login.default_bg = "#28a745"
    btn_login.pack(pady=10)
    on_hover(btn_login, "#1e7e34")

    btn_about = Button(
        button_frame,
        text="About",
        command=lambda: about_page(root, main_page),
        fg="white",
        bg="#6c757d",
        activebackground="#5a6268",
        activeforeground="white",
        **button_style
    )
    btn_about.default_bg = "#6c757d"
    btn_about.pack(pady=10)
    on_hover(btn_about, "#5a6268")

    # Footer
    footer_frame = Frame(root, bg="#e8f0f7")
    footer_frame.pack(side=BOTTOM, pady=20)

    Label(
        footer_frame,
        text="© 2025 Personal Finance Manager. All Rights Reserved.",
        font=("Arial", 10),
        fg="#888888",
        bg="#e8f0f7"
    ).pack()


if __name__ == "__main__":
    root = Tk()
    centerWin(root, 600, 600)
    main_page(root)
    root.mainloop()
