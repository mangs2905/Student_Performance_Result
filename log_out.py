from tkinter import *
from tkinter import messagebox

class LogoutPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Logout Page")
        self.root.geometry("300x150+600+300")
        self.root.config(bg="white")
        
        title = Label(self.root, text="Logout", font=("goudy old style", 20, "bold"), bg="#330154", fg="white")
        title.pack(side=TOP, fill=X)
        
        btn_logout = Button(self.root, text="Logout", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=100, y=60, width=100, height=40)
    
    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = LogoutPage(root)
    root.mainloop()
