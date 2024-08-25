import tkinter as tk
import csv

class AdminPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Admin Panel")
        self.master.geometry("300x150")
        self.create_widgets()

    def create_widgets(self):
        self.login_button = tk.Button(self.master, text="Admin Login", command=self.show_login)
        self.login_button.pack(pady=20)

    def show_login(self):
        self.login_window = tk.Toplevel(self.master)
        self.login_window.title("Admin Login")
        self.login_window.geometry("300x150")

        self.username_label = tk.Label(self.login_window, text="Username:")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.login_window, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        # Check if the username and password are correct
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin123":
            self.show_report()
            self.login_window.destroy()
        else:
            self.login_error_label = tk.Label(self.login_window, text="Incorrect username or password.")
            self.login_error_label.pack(pady=10)

    def show_report(self):
        self.report_window = tk.Toplevel(self.master)
        self.report_window.title("Attendance Report")
        self.report_window.geometry("300x150")

        self.report_label = tk.Label(self.report_window, text="Attendance Report")
        self.report_label.pack(pady=10)

        with open("attendance.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["Name"]
                attendance = row["Attendance"]
                report_line = f"{name}: {attendance}"
                self.report_line_label = tk.Label(self.report_window, text=report_line)
                self.report_line_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPanel(master=root)
    app.mainloop()