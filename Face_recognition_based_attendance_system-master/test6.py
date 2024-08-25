import tkinter as tk
import os
import csv
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile

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
    attendance_table.delete(*attendance_table.get_children())
    for filename in os.listdir("Mainattendance"):
        if filename.startswith(subject):
            with open(os.path.join("Mainattendance", filename)) as f:
                reader = csv.reader(f)
                next(reader) # skip header row
                for row in reader:
                    if row[0] == student_id_entry.get() and len(row[0])>0:
                        attendance_table.insert("", "end", values=row)
        attendance_table.pack()

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
student_id_label = tk.Label(attendance_frame, text="Enter student ID:")
student_id_entry = tk.Entry(attendance_frame)
attendance_table = ttk.Treeview(attendance_frame, columns=("ID", "Name", "Date", "Time"))
attendance_table.heading("ID", text="ID")
attendance_table.heading("Name", text="Name")
attendance_table.heading("Date", text="Date")
attendance_table.heading("Time", text="Time")
subject_dropdown.bind("<<ComboboxSelected>>", handle_subject_select)

subject_label.pack()
subject_dropdown.pack()
student_id_label.pack()
student_id_entry.pack()

# Pack the login page by default
login_frame.pack()

root.mainloop()
