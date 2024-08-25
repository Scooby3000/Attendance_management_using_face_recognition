from tkinter import *
import csv

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.geometry("500x400")

        # Creating menu bar
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # Creating login menu
        login_menu = Menu(menu_bar, tearoff=0)
        login_menu.add_command(label="Admin Login", command=self.admin_login)
        menu_bar.add_cascade(label="Login", menu=login_menu)

    def admin_login(self):
        # Creating login page
        login_window = Toplevel(self.root)
        login_window.title("Admin Login")
        login_window.geometry("300x200")

        # Creating username and password labels and entry fields
        Label(login_window, text="Username: ").grid(row=0, column=0, padx=10, pady=10)
        username_entry = Entry(login_window)
        username_entry.grid(row=0, column=1)

        Label(login_window, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
        password_entry = Entry(login_window, show="*")
        password_entry.grid(row=1, column=1)

        # Creating login button
        login_button = Button(login_window, text="Login", command=lambda: self.attendance_report(login_window))
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def attendance_report(self, login_window):
        # Creating attendance report page
        report_window = Toplevel(self.root)
        report_window.title("Attendance Report")
        report_window.geometry("500x400")

        # Creating dropdown to select subject
        subjects = ["AI&DS", "DMBI", "IP", "WEBX", "WT"]
        subject_var = StringVar()
        subject_var.set(subjects[0])
        subject_dropdown = OptionMenu(report_window, subject_var, *subjects)
        subject_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # Creating labels and entry fields for student id and total no. of lectures
        Label(report_window, text="Student ID: ").grid(row=1, column=0, padx=10, pady=10)
        student_id_entry = Entry(report_window)
        student_id_entry.grid(row=1, column=1)

        Label(report_window, text="Total No. of Lectures: ").grid(row=2, column=0, padx=10, pady=10)
        lectures_entry = Entry(report_window)
        lectures_entry.grid(row=2, column=1)

        # Creating submit button
        submit_button = Button(report_window, text="Submit", command=lambda: self.display_report(report_window, subject_var.get(), student_id_entry.get(), int(lectures_entry.get())))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def display_report(self, report_window, subject, student_id, total_lectures):
        # Reading attendance data from csv file
        with open(f"Mainattendance/{subject}.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                if row["ID"] == student_id:
                    data.append(row)

               # Creating table to display attendance data
        table_frame = Frame(report_window)
        table_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        Label(table_frame, text="Date").grid(row=0, column=0, padx=5, pady=5)
        Label(table_frame, text="Attendance").grid(row=0, column=1, padx=5, pady=5)

        for i, row in enumerate(data):
            Label(table_frame, text=row["Date"]).grid(row=i+1, column=0, padx=5, pady=5)
            Label(table_frame, text=row["Attendance"]).grid(row=i+1, column=1, padx=5, pady=5)

        # Calculating attendance percentage
        present_count = 0
        for row in data:
            if row["Attendance"] == "Present":
                present_count += 1

        attendance_percentage = present_count / total_lectures * 100

        # Creating label to display attendance percentage
        Label(report_window, text=f"Attendance Percentage: {attendance_percentage:.2f}%").grid(row=5, column=0, columnspan=2, pady=10)

root = Tk()
admin_panel = AdminPanel(root)
root.mainloop()
