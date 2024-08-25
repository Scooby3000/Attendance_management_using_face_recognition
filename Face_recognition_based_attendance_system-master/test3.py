import tkinter as tk
import csv

class AdminPanel:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x300")
        self.master.title("Admin Panel")

        self.admin_label = tk.Label(self.master, text="Admin Login")
        self.admin_label.pack(pady=10)

        self.admin_button = tk.Button(self.master, text="Login", command=self.login)
        self.admin_button.pack()

    def login(self):
        self.login_window = tk.Toplevel(self.master)
        self.login_window.geometry("300x300")
        self.login_window.title("Login Page")

        self.username_label = tk.Label(self.login_window, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)

        self.submit_button = tk.Button(self.login_window, text="Submit", command=self.attendance_report)
        self.submit_button.pack(pady=10)

    def attendance_report(self):
        self.report_window = tk.Toplevel(self.master)
        self.report_window.geometry("400x400")
        self.report_window.title("Attendance Report")

        self.subject_label = tk.Label(self.report_window, text="Select Subject:")
        self.subject_label.pack(pady=10)

        self.subject_options = ["AI&DS", "DMBI", "IP", "WEBX", "WT"]
        self.subject_dropdown = tk.OptionMenu(self.report_window, tk.StringVar(), *self.subject_options)
        self.subject_dropdown.pack(pady=5)

        self.generate_button = tk.Button(self.report_window, text="Generate Report", command=self.generate_report)
        self.generate_button.pack(pady=10)

    def generate_report(self):
        subject = self.subject_dropdown.cget("text")
        filename = "./Mainattendance/{}.csv".format(subject)

        with open(filename, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # skip header
            attendance_dict = {}

            for row in csv_reader:
                if row[1] not in attendance_dict:
                    attendance_dict[row[1]] = [0, 0]

                attendance_dict[row[1]][0] += 1
                attendance_dict[row[1]][1] += int(row[3])

        report_string = ""
        for name, attendance in attendance_dict.items():
            percentage = (attendance[1]/attendance[0])*100
            report_string += "{}: {:.2f}%\n".format(name, percentage)

        self.report_text = tk.Text(self.report_window, height=20, width=40)
        self.report_text.pack()
        self.report_text.insert(tk.END, report_string)

root = tk.Tk()
app = AdminPanel(root)
root.mainloop()
