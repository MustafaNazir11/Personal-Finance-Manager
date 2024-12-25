import tkinter as tk

def about_page(root):
    for widget in root.winfo_children():
        widget.destroy()
    window_H, window_W = 600, 800
    screen_H = root.winfo_screenheight() #height of device (laptop,PC) screen
    screen_W = root.winfo_screenwidth()#width of device (laptop,PC) screen
    Position_V = int(screen_H/2 -window_H/2) #Vertical Position of the window
    Position_H = int(screen_W/2 - window_W/2)
    root.title("About Personal Finance Manager")
    root.geometry(f"{window_W}x{window_H}+{Position_H}+{Position_V}")

    fixed_font = ("Courier", 14)
    bold_font = ("Courier", 14, "bold")
    heading_font = ("Helvetica", 18, "bold")
    excited_font = ("Arial", 16, "italic bold")

    canvas = tk.Canvas(root, bg="#2C2C2C")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas, bg="#2C2C2C")

    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="n")

    label_title = tk.Label(
        frame,
        text="About the Personal Finance Manager App",
        font=heading_font,
        fg="#FFA500",
        bg="#2C2C2C"
    )
    label_title.pack(pady=10)

    label_description = tk.Label(
        frame,
        text=(
            "Take Control of Your Finances with Ease\n\n"
            "Welcome to the Personal Finance Manager app—a comprehensive\n"
            "and user-friendly desktop tool designed to help you manage\n"
            "your money smarter. Whether you're keeping track of your daily\n"
            "expenses, setting monthly budgets, or planning for future financial\n"
            "goals, our app offers everything you need to stay organized and in\n"
            "control of your finances. With an easy-to-navigate interface and\n"
            "powerful features, the app ensures you can make informed financial\n"
            "decisions at any time."
        ),
        font=fixed_font,
        justify="center",
        wraplength=750,
        fg="white",
        bg="#2C2C2C"
    )
    label_description.pack(pady=10)

    label_features_title = tk.Label(
        frame,
        text="What Does This App Do?",
        font=heading_font,
        fg="#FFD700",
        bg="#2C2C2C"
    )
    label_features_title.pack(pady=10)

    label_features = tk.Label(
        frame,
        text=(
            "💸 Expense Tracking:\n"
            "    - Log all your income and expenses manually in a seamless manner.\n"
            "    - Categorize each transaction into clear categories (e.g., groceries, utilities, entertainment).\n\n"
            "📊 Budget Management:\n"
            "    - Set monthly budgets for different categories, ensuring you stay on track with your financial goals.\n"
            "    - Receive alerts when you're approaching or exceeding your set budget limits.\n\n"
            "📈 Data Visualization:\n"
            "    - Gain clear visual insights into your financial health and habits with the app’s powerful visualization tools.\n\n"
            "💾 Secure Data Storage:\n"
            "    - Your financial data is securely stored locally, ensuring that your information stays private.\n"
        ),
        font=fixed_font,
        justify="center",
        wraplength=750,
        fg="white",
        bg="#2C2C2C"
    )
    label_features.pack(pady=10)

    label_benefits_register_title = tk.Label(
        frame,
        text="Benefits of Using the App & How to Register",
        font=heading_font,
        fg="#00FF00",
        bg="#2C2C2C"
    )
    label_benefits_register_title.pack(pady=10)

    label_benefits_register = tk.Label(
        frame,
        text=(
            "📅 Stay Organized: Easily manage your financial activities.\n\n"
            "🔒 Secure and Private: Rest assured your data is safe.\n\n"
            "🚀 Improve Financial Health: Understand and optimize spending patterns.\n\n"
            "🕒 Save Time: User-friendly interface for efficient management.\n\n"
            "📊 Visual Clarity: Gain actionable insights with visual reports."
        ),
        font=fixed_font,
        justify="center",
        wraplength=750,
        fg="white",
        bg="#2C2C2C"
    )
    label_benefits_register.pack(pady=10)

    label_excited = tk.Label(
        frame,
        text=(
            "🚀 Start Your Financial Journey Today!\n"
            "    - Take control of your finances and achieve your goals with our app. 🌟"
        ),
        font=excited_font,
        justify="center",
        wraplength=750,
        fg="#FF4500",
        bg="#2C2C2C"
    )
    label_excited.pack(pady=20)

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root.bind_all("<MouseWheel>", on_mouse_wheel)

    root.mainloop()
