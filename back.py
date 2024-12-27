def navigate_to(root, next_page):

    for widget in root.winfo_children():
        widget.destroy()
    next_page(root)
