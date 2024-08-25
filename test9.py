from tkinter import *
import pandas as pd

# create tkinter window
window = Tk()
window.geometry("500x300")

# create login page
def login():
    user = username_entry.get()
    password = password_entry.get()
    if user == "admin" and password == "password":
        # show attendance page
        login_frame.destroy()
        attendance_frame.pack(pady=20)
    else:
        # show error message
        error_label = Label(login_frame, text="Invalid username or password")
        error_label.pack(pady=10)

# create login frame
login_frame = Frame(window)
login_frame.pack(pady=50)

# add username and password fields
username_label = Label(login_frame, text="Username:")
username_label.pack()
username_entry = Entry(login_frame)
username_entry.pack()

password_label = Label(login_frame, text="Password:")
password_label.pack()
password_entry = Entry(login_frame, show="*")
password_entry.pack()

# add login button
login_button = Button(login_frame, text="Login", command=login)
login_button.pack(pady=10)

# create attendance frame
attendance_frame = Frame(window)

# add subject dropdown
subject_label = Label(attendance_frame, text="Select Subject:")
subject_label.pack()
options = ["AI&DS", "DMBI", "IP", "WEBX", "WT"]
subject_dropdown = OptionMenu(attendance_frame, StringVar(), *options)
subject_dropdown.pack()

# add student ID and lectures occurred fields
id_label = Label(attendance_frame, text="Enter Student ID:")
id_label.pack()
id_entry = Entry(attendance_frame)
id_entry.pack()

lectures_label = Label(attendance_frame, text="Enter Total Lectures Occurred:")
lectures_label.pack()
lectures_entry = Entry(attendance_frame)
lectures_entry.pack()

# add submit button
def submit():
    # read data from CSV file
    subject = subject_dropdown.cget("text")
    df = pd.read_csv(f"Mainattendence/{subject}.csv")

    # filter data based on student ID
    id = id_entry.get()
    attendance = df.loc[df['Id'] == int(id)]

    # calculate attendance percentage
    total_lectures = int(lectures_entry.get())
    num_attendance = len(attendance)
    attendance_percent = round((num_attendance / total_lectures) * 100, 2)

    # create table
    table_frame = Frame(attendance_frame)
    table_frame.pack(pady=20)

    cols = ("Id", "Name", "Date", "Time")
    for i, col in enumerate(cols):
        Label(table_frame, text=col, bg="white", relief=RIDGE, width=15).grid(row=0, column=i)
    for i, row in attendance.iterrows():
        for j, col in enumerate(cols):
            Label(table_frame, text=row[col], bg="white", relief=RIDGE, width=15).grid(row=i+1, column=j)

    # add attendance percentage
    attendance_percent_label = Label(attendance_frame, text=f"Attendance Percentage: {attendance_percent}%")
    attendance_percent_label.pack(pady=10)

submit_button = Button(attendance_frame, text="Submit", command=submit)
submit_button.pack(pady=10)

# run tkinter event loop
window.mainloop()
