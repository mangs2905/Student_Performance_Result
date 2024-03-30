from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("400x300+500+150")
        self.root.config(bg="white")
        
        title = Label(self.root, text="Login", font=("goudy old style", 20, "bold"), bg="#330154", fg="white")
        title.pack(side=TOP, fill=X)
        
        self.username = StringVar()
        self.password = StringVar()
        
        lbl_username = Label(self.root, text="Username", font=("goudy old style", 15, "bold"), bg="white")
        lbl_username.place(x=50, y=60)
        self.txt_username = Entry(self.root, textvariable=self.username, font=("goudy old style", 15), bg="lightyellow")
        self.txt_username.place(x=200, y=60)
        
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 15, "bold"), bg="white")
        lbl_password.place(x=50, y=110)
        self.txt_password = Entry(self.root, textvariable=self.password, font=("goudy old style", 15), bg="lightyellow", show="*")
        self.txt_password.place(x=200, y=110)
        
        btn_login = Button(self.root, text="Login", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.login)
        btn_login.place(x=150, y=160, width=100, height=40)
        
    def login(self):
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.root.destroy()
            self.app = StudentManagementSystem()
        else:
            messagebox.showerror("Error", "Invalid username or password")

class StudentManagementSystem:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Rest of your code goes here...

if __name__ == "__main__":
    root = Tk()
    obj = LoginPage(root)
    root.mainloop()
