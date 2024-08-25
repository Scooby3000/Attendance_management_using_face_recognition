import tkinter as tk
from tkinter import ttk
import os
import csv

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
    attendance_data[subject] = {}
    for filename in os.listdir("Mainattendance"):
        if filename.startswith(subject):
            with open(os.path.join("Mainattendance", filename)) as f:
                reader = csv.reader(f)
                next(reader) # skip header row
                for row in reader:
                    student_id, student_name, date, time = row
                    if student_name not in attendance_data[subject]:
                        attendance_data[subject][student_name] = {
                            "present": 0,
                            "total": 0
                        }
                    attendance_data[subject][student_name]["total"] += 1
                    if time != "ABSENT":
                        attendance_data[subject][student_name]["present"] += 1
    generate_report()

# Function to generate the attendance report
def generate_report():
    report_text.delete(1.0, tk.END)
    subject = selected_subject.get()
    report_text.insert(tk.END, f"Attendance report for {subject}:\n\n")
    for student, data in attendance_data[subject].items():
        percent = 100 * data["present"] / data["total"]
        report_text.insert(tk.END, f"{student}: {percent:.2f}% attendance\n")

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
report_text = tk.Text(attendance_frame, height=20, width=50)
subject_dropdown.bind("<<ComboboxSelected>>", handle_subject_select)

subject_label.pack()
subject_dropdown.pack()
report_text.pack()

# Pack the login page by default
login_frame.pack()

root.mainloop()
