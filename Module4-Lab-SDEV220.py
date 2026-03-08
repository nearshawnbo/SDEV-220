import sqlite3

DB_NAME = "library.db"
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


#Initializes the Database
def initialize_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        #Books Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT
            )
        );
        """)
       

# Book CRUD 6 Functions
def add_book(title, author, publisher):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Books (title, author, publisher)
            VALUES (?, ?, ?)
        """, (title, author, publisher))
        conn.commit()

def delete_book(book_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
        conn.commit()

def update_book(title, author, publisher, book_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE Books SET title =?, author = ?, publisher = ?, available_copies = ?
                         WHERE book_id = ?""",(title, author, publisher ,book_id, ))
        conn.commit()

def get_all_books():
     with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        return cursor.fetchall()

def get_book_by_id(book_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE book_id = ?", (book_id,))
        return cursor.fetchone()

def search_book(title=None, book_id=None, author=None, publisher=None):
    with get_connection() as conn:
        cursor = conn.cursor()

        if book_id is not None:
            cursor.execute("SELECT * FROM Books WHERE book_id = ?", (book_id,))
        elif title is not None:
            cursor.execute("SELECT * FROM Books WHERE title LIKE ?", (f"%{title}%",))
        elif author is not None:
            cursor.execute("SELECT * FROM Books WHERE author LIKE ?", (f"%{author}%",))
        elif publisher is not None:
            cursor.execute("SELECT * FROM Books WHERE publisher LIKE ?", (f"%{publisher}%",))
        else:
            return None

        return cursor.fetchall() 







              

