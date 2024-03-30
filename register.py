# from tkinter import *
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
# import pymysql

# class Register:
#     def __init__(self,root):
#         self.root = root
#         self.root.title("Registration Window")
#         self.root.geometry("1350x700+0+0")
#         self.root.config(bg="white")
        
#         #====Background_Image======
#         self.bg = ImageTk.PhotoImage(file="Images/result.jpg")
#         bg = Label(self.root, image=self.bg).place(x=250, y=0, width=1, height=1)
        
#         #====Left_Image=====
#         self.left = ImageTk.PhotoImage(file="Images/result.jpg")
#         left = Label(self.root, image= self.left).place(x=80, y=100, width=400, height=500)
        
#         #====Register_Frame=======
#         frame1 = Frame(self.root, bg="white")
#         frame1.place(x=480, y=100, width=700, height=500)
        
#         title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white")
        
#         #===Row1============
        
#         f_name = Label(frame1, text=("First Name", 15, "bold"), bg="white")
#         self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
#         self.text_fname.place(x=50, y=130, width=250)
        
#         l_name = Label(frame1, text=("Last Name", 15, "bold"), bg="white")
#         self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
#         self.text_lname.place(x=50, y=130, width=250)

#=========================================================================================================================================

from tkinter import *
from tkinter import messagebox
import random

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x250")

        self.username_var = StringVar()
        self.password_var = StringVar()

        Label(root, text="Username").pack()
        Entry(root, textvariable=self.username_var).pack()
        Label(root, text="Password").pack()
        Entry(root, textvariable=self.password_var, show="*").pack()
        Button(root, text="Register", command=self.register_user).pack()

    def register_user(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username and password:
            with open("users.txt", "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "Username and password are required.")

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x250")

        self.username_var = StringVar()
        self.password_var = StringVar()

        Label(root, text="Username").pack()
        Entry(root, textvariable=self.username_var).pack()
        Label(root, text="Password").pack()
        Entry(root, textvariable=self.password_var, show="*").pack()
        Button(root, text="Login", command=self.login_user).pack()
        Button(root, text="Forgot Password", command=self.forgot_password).pack()

    def login_user(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username and password:
            with open("users.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    stored_username, stored_password = line.strip().split(",")
                    if username == stored_username and password == stored_password:
                        messagebox.showinfo("Success", "Login successful!")
                        return
            messagebox.showerror("Error", "Invalid username or password.")
        else:
            messagebox.showerror("Error", "Username and password are required.")

    def forgot_password(self):
        username = self.username_var.get()

        if username:
            with open("users.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    stored_username, stored_password = line.strip().split(",")
                    if username == stored_username:
                        messagebox.showinfo("Password", f"Your password is: {stored_password}")
                        return
            messagebox.showerror("Error", "Username not found.")
        else:
            messagebox.showerror("Error", "Username is required.")

def main():
    root = Tk()
    Register(root)
    Login(root)
    root.mainloop()

if __name__ == "__main__":
    main()

