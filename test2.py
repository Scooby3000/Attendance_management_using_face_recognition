import tkinter as tk
import csv

class AttendanceReport:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Attendance Report")

        self.subjects = ["AI&DS", "DMBI", "IP", "WEBX", "WT"]

        self.dropdown = tk.StringVar(self.root)
        self.dropdown.set("Select Subject")

        self.select_subject = tk.OptionMenu(self.root, self.dropdown, *self.subjects)
        self.select_subject.pack(pady=20)

        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_report)
        self.generate_button.pack()

        self.report = tk.Label(self.root, text="")
        self.report.pack(pady=20)

    def generate_report(self):
        selected_subject = self.dropdown.get()
        if selected_subject == "Select Subject":
            return

        csv_file_path = f"Mainattendance/{selected_subject}.csv"
        with open(csv_file_path, "r") as f:
            csv_reader = csv.reader(f)
            next(csv_reader) # skip header row
            data = {}
            for row in csv_reader:
                id, name, date, time = row
                if name not in data:
                    data[name] = {
                        "total": 0,
                        "present": 0
                    }
                data[name]["total"] += 1
                if time != "":
                    data[name]["present"] += 1

        report_text = f"Attendance Report for {selected_subject}\n\n"
        for name in data:
            percentage = round(data[name]["present"] / data[name]["total"] * 100, 2)
            report_text += f"{name}: {percentage}%\n"

        self.report.config(text=report_text)


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Login")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.root.destroy()
            root = tk.Tk()
            app = AttendanceReport(root)
            root.mainloop()


root = tk.Tk()
app = Login(root)
root.mainloop()
