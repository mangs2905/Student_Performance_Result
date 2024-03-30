from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from books import BookReader

class SPR:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="white")
        #====icons====
        self.logo_dash = ImageTk.PhotoImage(file="Images/edu_logo.png")
        
        #====title====
        title = Label(text="Student Management System", font=("goudy old style", 20, "bold"), padx=10, image=self.logo_dash, compound=LEFT ,bg="#033054", fg="white").place(x=0,y=0, relwidth=1, height=50)
        
        #====Menu====
        M_Frame = LabelFrame(self.root,text="Menues", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)
        
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="student", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="result", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="view", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=680, y=5, width=200, height=40)
        btn_books = Button(M_Frame, text="books", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2", command=self.add_books).place(x=900, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="logout", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2").place(x=1120, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="exit", font=("goudy old style", 15), bg="#0b5377", fg="white", cursor="hand2").place(x=1340, y=5, width=200, height=40)
        
        #====content_window====
        self.bg_img = Image.open("Images/bg_school.jpeg")
        self.bg_img = self.bg_img.resize((920,320), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)
        
        #====Update_Details=====
        self.lbl_course = Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)
        self.lbl_student = Label(self.root, text="Total student\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0466ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)
        self.lbl_result = Label(self.root, text="Total result\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)
        
        
        #====Footer====
        footer = Label(text="SMS-Student Management System\nContact Us for Any technical Issue: 7972746215", font=("goudy old style", 12), padx=10, bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)
        
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)
        
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)
        
    def add_books(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BookReader(self.new_win)                



if __name__=="__main__":
    root = Tk()
    obj = SPR(root)
    root.mainloop()