# import sqlite3
# def create_db():
#     con = sqlite3.connect(database="SPR.db")
#     cur = con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges text, description text)")
#     con.commit()
    
#     cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,course text,state text,city text,pin text,address text)")
#     con.commit()
    
#     cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text, marks_ob text, full_marks text, per text)")
#     con.commit()
        
#     con.close()
    
    
    
# create_db()
import sqlite3

def create_books_db():
    # Create a connection to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('books.db')

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Create a table named 'books' with columns 'title' and 'content'
    cur.execute('''CREATE TABLE IF NOT EXISTS books
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT)''')

    # Sample books data (title, content)
    books_data = [
        ("Book 1", "This is the content of Book 1."),
        ("Book 2", "This is the content of Book 2."),
        ("Book 3", "This is the content of Book 3."),
        # Add more books as needed
    ]

    # Insert the sample books data into the 'books' table
    cur.executemany("INSERT INTO books (title, content) VALUES (?, ?)", books_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database 'books.db' created successfully with table 'books' populated.")

def create_SPR_db():
    con = sqlite3.connect(database="SPR.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration TEXT, charges TEXT, description TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, gender TEXT, dob TEXT, contact TEXT, course TEXT, state TEXT, city TEXT, pin TEXT, address TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll TEXT, name TEXT, course TEXT, marks_ob TEXT, full_marks TEXT, per TEXT)")
    con.commit()
    con.close()

# Create books database and populate with sample data
create_books_db()

# Create SPR database and its tables
create_SPR_db()
