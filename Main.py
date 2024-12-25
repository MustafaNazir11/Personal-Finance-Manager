from tkinter import *
from register import register
from login import login
from about_page import about_page

root = Tk()
root.title("Personal Finance Manager")

window_W, window_H = 500, 400 

screen_H = root.winfo_screenheight() #height of device (laptop,PC) screen
screen_W = root.winfo_screenwidth()#width of device (laptop,PC) screen
Position_V = int(screen_H/2 -window_H/2) #Vertical Position of the window
Position_H = int(screen_W/2 - window_W/2) #Horizontal Position of the window
root.geometry(f"{window_W}x{window_H}+{Position_H}+{Position_V}")

root.configure(bg="#d3d3d3")





Label(
    root,
    text="PERSONAL FINANCE TRACKER",
    font=("Helvetica", 22, "bold","underline"),
    fg="#000080",
    bg="#d3d3d3"
).pack(pady=30)

Button(
    root,
    text="Register",
    command=lambda: register(root),
    fg="white",
    bg="#004080",
    font=("Helvetica", 14, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=4
).pack(pady=15)

Button(
    root,
    text="Login",
    command=lambda: login(root),
    fg="white",
    bg="#004080",
    font=("Helvetica", 14, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=4
).pack(pady=15)

Button(
    root,
    text="About",
    command=lambda: about_page(root),
    fg="white",
    bg="#2c2c2c",
    font=("Helvetica", 14, "bold"),
    width=15,
    height=2,
    relief="raised",
    bd=4
).pack(pady=15)
print(screen_W,window_W)
root.mainloop()
