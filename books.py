from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class BookReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Reader")
        self.root.geometry("600x400")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="Available Books", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10,y=15, width=580, height=50)
        
        # Book List
        self.book_listbox = Listbox(self.root, font=("goudy old style", 15), bg="lightyellow", bd=2, relief=GROOVE)
        self.book_listbox.place(x=10, y=80, width=580, height=250)
        self.book_listbox.bind('<<ListboxSelect>>', self.show_content)

        # Load Books
        self.load_books()

        # Content Text
        self.content_text = Text(self.root, font=("goudy old style", 12), bg="lightblue", bd=2, relief=GROOVE)
        self.content_text.place(x=10, y=340, width=580, height=250)

        # Question Button
        btn_question = Button(self.root, text="Ask a Question", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.ask_question)
        btn_question.place(x=200, y=300, width=200, height=35)

    def load_books(self):
        try:
            con = sqlite3.connect(database="books.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM books")
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.book_listbox.insert(END, row[1])
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading books: {str(ex)}")

    def show_content(self, event):
        try:
            selected_book = self.book_listbox.get(self.book_listbox.curselection())
            con = sqlite3.connect(database="books.db")
            cur = con.cursor()
            cur.execute("SELECT content FROM books WHERE title=?", (selected_book,))
            row = cur.fetchone()
            if row:
                self.content_text.delete("1.0", END)
                self.content_text.insert(END, row[0])
            else:
                self.content_text.delete("1.0", END)
                self.content_text.insert(END, "Content not available")
        except Exception as ex:
            messagebox.showerror("Error", f"Error loading content: {str(ex)}")

    def ask_question(self):
        selected_book = self.book_listbox.get(self.book_listbox.curselection())
        if selected_book:
            messagebox.showinfo("Ask a Question", f"Please ask your question related to '{selected_book}'.")

if __name__=="__main__":
    root = Tk()
    obj = BookReader(root)
    root.mainloop()
