import tkinter as tk

def about_page(root):
    # Create the main window
    for widget in root.winfo_children():
        widget.destroy()
    root.title("About Personal Finance Manager")
    root.geometry("800x600")  # Initial size

    # Set different fonts for emphasis
    fixed_font = ("Courier", 14)
    bold_font = ("Courier", 14, "bold")
    heading_font = ("Helvetica", 18, "bold")
    excited_font = ("Arial", 16, "italic", "bold")

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas)

    # Configure the canvas and scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Add title
    label_title = tk.Label(frame, text="          About the Personal Finance Manager App          ", 
                           font=heading_font, fg="darkblue")
    label_title.pack(pady=10, anchor="center")

    # Description of the app
    label_description = tk.Label(frame, text=(
        "Take Control of Your Finances with Ease\n\n"
        "Welcome to the Personal Finance Manager app—a comprehensive\n"
        "and user-friendly desktop tool designed to help you manage\n"
        "your money smarter. Whether you're keeping track of your daily\n"
        "expenses, setting monthly budgets, or planning for future financial\n"
        "goals, our app offers everything you need to stay organized and in\n"
        "control of your finances. With an easy-to-navigate interface and\n"
        "powerful features, the app ensures you can make informed financial\n"
        "decisions at any time."
    ), font=fixed_font, justify="center", wraplength=750, fg="black")
    label_description.pack(pady=10, anchor="center")

    # Features title
    label_features_title = tk.Label(frame, text="          What Does This App Do?          ",
                                    font=heading_font, fg="blue")
    label_features_title.pack(pady=10, anchor="center")

    # Features list
    label_features = tk.Label(frame, text=(
        "💸 Expense Tracking:\n"
        "    - Log all your income and expenses manually in a seamless manner.\n"
        "    - Categorize each transaction into clear categories (e.g., groceries, utilities, entertainment).\n"
        "    - Review your spending habits over time to identify areas where you might be able to cut back or save more.\n\n"
        "📊 Budget Management:\n"
        "    - Set monthly budgets for different categories, ensuring you stay on track with your financial goals.\n"
        "    - Receive alerts when you're approaching or exceeding your set budget limits, helping you stay disciplined and make informed decisions.\n"
        "    - Manage your finances with ease and work toward achieving financial stability by adhering to your budgets.\n\n"
        "📈 Data Visualization:\n"
        "    - Gain clear visual insights into your financial health and habits with the app’s powerful visualization tools.\n"
        "    - Use interactive bar charts and pie charts to view your spending patterns and savings trends, generated through Matplotlib.\n"
        "    - Make better financial decisions based on the detailed analytics, which will help you adjust your habits for more financial success.\n\n"
        "💾 Secure Data Storage:\n"
        "    - Your financial data is securely stored locally, ensuring that your information stays private and accessible only to you.\n"
        "    - Save your financial records in CSV files, providing a simple yet efficient way to keep track of your expenses and budgets without any unnecessary complexity."
    ), font=fixed_font, justify="left", wraplength=750, fg="black")
    label_features.pack(pady=10, anchor="center")

    # Merged Benefits and Registration section
    label_benefits_register_title = tk.Label(frame, text="          Benefits of Using the Personal Finance Manager\n\n"
                                                          "                & How to Register          ",
                                              font=heading_font, fg="blue")
    label_benefits_register_title.pack(pady=10, anchor="center")

    label_benefits_register = tk.Label(frame, text=(
        "📅 Stay Organized: Easily manage your daily, weekly, and monthly financial activities with the intuitive tools provided. Stay on top of your expenses and budgets without hassle.\n\n"
        "🔒 Secure and Private: Rest assured knowing that all your financial data is stored securely and privately on your device, with no risk of unauthorized access.\n\n"
        "🚀 Improve Financial Health: Understand your spending patterns more clearly and make informed financial decisions based on visual reports, helping you work toward better financial health.\n\n"
        "🕒 Save Time: With the app's user-friendly interface, managing your finances becomes a quick and efficient process, so you can focus on other important aspects of life.\n\n"
        "📊 Visual Clarity: Visual reports offer easy-to-understand insights, allowing you to grasp complex data in an instant and take immediate action when necessary.\n\n"
        
        "Getting started with the Personal Finance Manager is simple and straightforward! Just follow these easy steps to create your account and begin managing your finances:\n\n"
        
        "Fill Out the Registration Form:\n"
        "    - Provide a valid email address and choose a secure password to protect your account.\n"
        "    - You can enter additional details if prompted, but it’s optional to get started.\n\n"
        
        "Verify Your Email:\n"
        "    - Confirm your registration by clicking the verification link that will be sent to your email inbox.\n\n"
        
        "Log In and Start Managing Your Finances:\n"
        "    - Once you’ve verified your email, you’ll have full access to the app. Log in and begin logging your expenses, setting budgets, and tracking your spending and savings goals."
    ), font=fixed_font, justify="left", wraplength=750, fg="black")
    label_benefits_register.pack(pady=10, anchor="center")

    # Start Financial Journey section with excitement
    label_excited = tk.Label(frame, text=(
        "🚀 Start Your Financial Journey Today!\n"
        "    - Don't wait any longer! Take control of your finances NOW and unlock the full potential of the Personal Finance Manager. With its amazing features, you'll be empowered to make smarter financial decisions and work toward achieving your financial freedom! 🌟"
    ), font=excited_font, justify="center", wraplength=750, fg="red")
    label_excited.pack(pady=20, anchor="center")

    # Update the scroll region to encompass all widgets
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Bind the mouse scroll to the canvas
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    root.bind_all("<MouseWheel>", on_mouse_wheel)

    root.mainloop()

# Call the about page function to run the app

