from tkinter import *
import pandas as pd

class AdminPanel:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Panel")
        self.master.geometry("400x200")
        self.login_button = Button(self.master, text="Admin Login", command=self.login_page)
        self.login_button.pack(pady=20)

    def login_page(self):
        self.login_window = Toplevel(self.master)
        self.login_window.title("Admin Login")
        self.login_window.geometry("300x150")
        self.username_label = Label(self.login_window, text="Username:")
        self.username_label.pack(pady=10)
        self.username_entry = Entry(self.login_window)
        self.username_entry.pack()
        self.password_label = Label(self.login_window, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = Entry(self.login_window, show="*")
        self.password_entry.pack()
        self.login_button = Button(self.login_window, text="Login", command=self.attendance_report_page)
        self.login_button.pack(pady=20)

    def attendance_report_page(self):
        self.login_window.destroy()
        self.attendance_window = Toplevel(self.master)
        self.attendance_window.title("Attendance Report")
        self.attendance_window.geometry("500x300")
        self.subject_label = Label(self.attendance_window, text="Select Subject:")
        self.subject_label.pack(pady=10)
        self.subject_list = ["AI&DS", "DMBI", "IP", "WEBX", "WT"]
        self.subject_dropdown = OptionMenu(self.attendance_window, StringVar(), *self.subject_list)
        self.subject_dropdown.pack()
        self.student_id_label = Label(self.attendance_window, text="Enter Student ID:")
        self.student_id_label.pack(pady=10)
        self.student_id_entry = Entry(self.attendance_window)
        self.student_id_entry.pack()
        self.total_lectures_label = Label(self.attendance_window, text="Enter Total Lectures:")
        self.total_lectures_label.pack(pady=10)
        self.total_lectures_entry = Entry(self.attendance_window)
        self.total_lectures_entry.pack()
        self.submit_button = Button(self.attendance_window, text="Submit", command=self.display_attendance_report)
        self.submit_button.pack(pady=20)

    def display_attendance_report(self):
        subject = self.subject_dropdown.cget("text")
        student_id = self.student_id_entry.get()
        total_lectures = int(self.total_lectures_entry.get())
        file_name = subject + ".csv"
        try:
            df = pd.read_csv("Mainattendance/" + file_name)
            student_data = df.loc[df['ID'] == student_id]
            attendance_percentage = (student_data.sum(axis=1) - 1) / total_lectures * 100
            attendance_percentage = round(attendance_percentage.values[0], 2)
            student_data = student_data.drop(columns=["ID", "Name"]).T
            student_data.columns = [student_id]
            student_data["Total Lectures"] = total_lectures
            student_data["Attendance Percentage"] = attendance_percentage
            self.attendance_table = Label(self.attendance_window, text=student_data.to_string())
            self.attendance_table.pack(pady=20)
        except FileNotFoundError:
            self.attendance_table = Label(self.attendance_window, text="Attendance data for this subject is not available!")
            self.attendance_table.pack(pady=20)

root = Tk()
admin_panel = AdminPanel(root)
root.mainloop()
