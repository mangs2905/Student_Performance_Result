import cv2
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sqlite3

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Attendance System")
        self.root.geometry("600x400")

        # Initialize database
        self.conn = sqlite3.connect('teacher_attendance.db')
        self.create_table()

        # Capture device setup
        self.capture = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Interface elements
        tk.Label(root, text="Teacher Attendance System", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(root, text="Capture Selfie", command=self.capture_selfie).pack(pady=10)
        tk.Button(root, text="Scan Fingerprint", command=self.scan_fingerprint).pack(pady=10)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS teachers
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          username TEXT NOT NULL,
                          password TEXT NOT NULL,
                          created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()

    def register_teacher(self, name, username, password):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO teachers (name, username, password) VALUES (?, ?, ?)", (name, username, password))
        self.conn.commit()
        messagebox.showinfo("Success", "Teacher registered successfully.")

    def authenticate_teacher(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM teachers WHERE username = ? AND password = ?", (username, password))
        teacher = cursor.fetchone()
        if teacher:
            messagebox.showinfo("Success", f"Welcome, {teacher[1]}!")
            return True
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            return False

    def capture_selfie(self):
        # Placeholder for selfie capture functionality
        messagebox.showinfo("Info", "Selfie captured successfully.")
        # Save selfie to a directory or process it further
        
        # Sample code to get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Selfie captured at:", current_time)

    def scan_fingerprint(self):
        # Placeholder for fingerprint scanning functionality
        messagebox.showinfo("Info", "Fingerprint scanned successfully.")
        # Process the scanned fingerprint
        
        # Sample code to get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Fingerprint scanned at:", current_time)

    def __del__(self):
        if hasattr(self, 'capture'):
            self.capture.release()

class TeacherRegistration:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Registration")
        self.root.geometry("400x200")

        # Interface elements
        tk.Label(root, text="Teacher Registration", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        tk.Label(root, text="Password:").pack()
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()
        tk.Button(root, text="Register", command=self.register).pack(pady=10)

    def register(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if name and username and password:
            attendance_system = AttendanceSystem(root)
            attendance_system.register_teacher(name, username, password)
            self.root.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

class TeacherLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Login")
        self.root.geometry("300x150")

        # Interface elements
        tk.Label(root, text="Teacher Login", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        tk.Label(root, text="Password:").pack()
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.pack()
        tk.Button(root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            attendance_system = AttendanceSystem(root)
            if attendance_system.authenticate_teacher(username, password):
                self.root.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

if __name__ == "__main__":
    root = tk.Tk()
    TeacherLogin(root)
    root.mainloop()
