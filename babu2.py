import tkinter as tk
from tkinter import messagebox
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {
    "student1": hash_password("pass123"),
    "teacher1": hash_password("teach456"),
    "admin": hash_password("adminpass")
}

roles = {
    "student1": "student",
    "teacher1": "teacher",
    "admin": "admin"
}

def login():
    username = entry_username.get()
    password = hash_password(entry_password.get())

    if username in users and users[username] == password:
        role = roles.get(username, "student")  # default to student
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()  # Close login window

        if role == "student":
            open_student_profile(username)
        else:
            open_other_dashboard(username, role)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_student_profile(username):
    profile = tk.Tk()
    profile.title("Student Profile")
    profile.geometry("350x300")

    # Example student data (can be dynamic)
    student_data = {
        "Name": "Deva Vardhan",
        "Roll No": "22KH1A0580",
        "Course": "B.Tech - Computer Science",
        "Year": "4th Year",
        "Email": "devavardhanbabu@gmail.com"
    }

    tk.Label(profile, text=f"Welcome, {username}", font=("Arial", 14, "bold")).pack(pady=10)

    for key, value in student_data.items():
        tk.Label(profile, text=f"{key}: {value}", font=("Arial", 11)).pack(pady=5)

    tk.Button(profile, text="Logout", command=profile.destroy).pack(pady=20)
    profile.mainloop()

def open_other_dashboard(username, role):
    win = tk.Tk()
    win.title(f"{role.capitalize()} Dashboard")
    win.geometry("300x150")
    tk.Label(win, text=f"{role.capitalize()} Dashboard for {username}", font=("Arial", 12)).pack(pady=20)
    tk.Button(win, text="Logout", command=win.destroy).pack(pady=10)
    win.mainloop()  # ✅ Fixed missing parenthesis

# --- Main Login Window ---

root = tk.Tk()
root.title("College Login Page")
root.geometry("300x220")

tk.Label(root, text="Username:").pack(pady=(20, 5))
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack(pady=(10, 5))
entry_password = tk.Entry(root, show="*")
entry_password.pack()

def toggle_password():
    if show_pass_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

show_pass_var = tk.BooleanVar()
tk.Checkbutton(root, text="Show Password", variable=show_pass_var, command=toggle_password).pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
