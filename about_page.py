import tkinter as tk
from utility import navigate_to

def about_page(root, home_page):
    for widget in root.winfo_children():
        widget.destroy()

    window_H, window_W = 600, 800
    screen_H = root.winfo_screenheight()
    screen_W = root.winfo_screenwidth()
    Position_V = int(screen_H / 2 - window_H / 2)
    Position_H = int(screen_W / 2 - window_W / 2)

    root.title("About Personal Finance Manager")
    root.geometry(f"{window_W}x{window_H}+{Position_H}+{Position_V}")
    root.configure(bg="#e8f0f7")

    fixed_font = ("Arial", 14)
    bold_font = ("Arial", 14, "bold")
    heading_font = ("Arial", 18, "bold")
    excited_font = ("Arial", 16, "italic bold")

    canvas = tk.Canvas(root, bg="#e8f0f7")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas, bg="#e8f0f7")

    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="n")

    label_title = tk.Label(
        frame,
        text="About the Personal Finance Manager App",
        font=heading_font,
        fg="#003366",
        bg="#e8f0f7"
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
        fg="#555555",
        bg="#e8f0f7"
    )
    label_description.pack(pady=10)

    label_features_title = tk.Label(
        frame,
        text="What Does This App Do?",
        font=heading_font,
        fg="#003366",
        bg="#e8f0f7"
    )
    label_features_title.pack(pady=10)

    label_features = tk.Label(
        frame,
        text=(
            "💸 Expense Tracking:\n"
            "    - Log all your income and expenses manually in a seamless manner.\n"
            "    - Categorize each transaction into clear categories.\n\n"
            "📊 Budget Management:\n"
            "    - Set monthly budgets for different categories.\n"
            "    - Receive alerts when you're approaching or exceeding budget limits.\n\n"
            "📈 Data Visualization:\n"
            "    - Gain clear visual insights into your financial health.\n\n"
            "💾 Secure Data Storage:\n"
            "    - Your financial data is securely stored locally."
        ),
        font=fixed_font,
        justify="center",
        wraplength=750,
        fg="#555555",
        bg="#e8f0f7"
    )
    label_features.pack(pady=10)

    label_benefits_register_title = tk.Label(
        frame,
        text="Benefits of Using the App & How to Register",
        font=heading_font,
        fg="#003366",
        bg="#e8f0f7"
    )
    label_benefits_register_title.pack(pady=10)

    label_benefits_register = tk.Label(
        frame,
        text=(
            "📅 Stay Organized: Easily manage your financial activities.\n\n"
            "🔒 Secure and Private: Rest assured your data is safe.\n\n"
            "🚀 Improve Financial Health: Understand and optimize spending patterns.\n\n"
            "⏳ Save Time: User-friendly interface for efficient management.\n\n"
            "📊 Visual Clarity: Gain actionable insights with visual reports."
        ),
        font=fixed_font,
        justify="center",
        wraplength=750,
        fg="#555555",
        bg="#e8f0f7"
    )
    label_benefits_register.pack(pady=10)

    label_excited = tk.Label(
        frame,
        text=(
            "🚀 Start Your Financial Journey Today!\n"
            "    - Take control of your finances and achieve your goals. 🌟"
        ),
        font=excited_font,
        justify="center",
        wraplength=750,
        fg="#003366",
        bg="#e8f0f7"
    )
    label_excited.pack(pady=20)

    button_back = tk.Button(
        frame,
        text="Back",
        command=lambda: navigate_to(root, home_page),
        font=("Arial", 14, "bold"),
        bg="#0078d7",
        fg="white",
        relief="flat",
        cursor="hand2",
        activebackground="#005bb5",
        activeforeground="white",
        width=10
    )
    button_back.pack(pady=20)

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root.bind_all("<MouseWheel>", on_mouse_wheel)