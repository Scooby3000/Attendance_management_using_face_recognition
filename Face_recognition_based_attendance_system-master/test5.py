import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Set up the main window
root = tk.Tk()
root.title("Admin Panel")

# Set up variables for the login page
username = tk.StringVar()
password = tk.StringVar()

# Set up variables for the attendance report page
selected_subject = tk.StringVar()
subjects = ["AI&DS", "DMBI", "IP", "WEBX", "WT"]
attendance_data = {}

# Function to handle the login button click
def handle_login():
    if username.get() == "admin" and password.get() == "admin123":
        login_frame.destroy()
        attendance_frame.pack()

# Function to handle the subject dropdown selection
def handle_subject_select(event):
    subject = selected_subject.get()
    filename = os.path.join("Mainattendance", f"{subject}.csv")
    if os.path.exists(filename):
        attendance_df = pd.read_csv(filename)
        attendance_table["columns"] = list(attendance_df.columns)
        attendance_table.delete(*attendance_table.get_children())
        for index, row in attendance_df.iterrows():
            attendance_table.insert("", "end", values=list(row))
    else:
        attendance_table.delete(*attendance_table.get_children())
        attendance_table.insert("", "end", values=["No data available for selected subject."])

# Set up the login page
login_frame = tk.Frame(root)
login_label = tk.Label(login_frame, text="Please enter admin credentials")
username_label = tk.Label(login_frame, text="Username:")
password_label = tk.Label(login_frame, text="Password:")
username_entry = tk.Entry(login_frame, textvariable=username)
password_entry = tk.Entry(login_frame, textvariable=password, show="*")
login_button = tk.Button(login_frame, text="Login", command=handle_login)

login_label.pack()
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()

# Set up the attendance report page
attendance_frame = tk.Frame(root)
subject_label = tk.Label(attendance_frame, text="Select a subject:")
subject_dropdown = ttk.Combobox(attendance_frame, values=subjects, textvariable=selected_subject)
attendance_table = ttk.Treeview(attendance_frame)
subject_dropdown.bind("<<ComboboxSelected>>", handle_subject_select)

subject_label.pack()
subject_dropdown.pack()
attendance_table.pack()

# Pack the login page by default
login_frame.pack()

root.mainloop()
