import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from homePage import HomePage
from journalPage import JournalPage
from reflectionsPage import ReflectionsPage
from signupPage import SignupPage 
from loginPage import LoginPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Journal Application")
        self.geometry("800x600")

        self.create_database()

        self.create_widgets()

    def create_database(self):
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect('./app/database/database.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Create a table for user data
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def create_widgets(self):
        # Configure the main frame to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create the main frame
        main_frame = ttk.Frame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Configure the main frame to expand
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        
        # Create the sidebar frame
        sidebar_frame = ttk.Frame(main_frame, width=50, )
        sidebar_frame.grid(row=0, column=0, sticky="ns")

        # Create the content frame
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # Add buttons to the sidebar
        btn_home = ttk.Button(sidebar_frame, width=10,text="Homepage", command=self.show_homepage)
        btn_home.pack(fill=tk.X, pady=5)
       

        btn_signup = ttk.Button(sidebar_frame, text="Login", command=self.show_login)
        btn_signup.pack(fill=tk.X, pady=5)
        

        btn_signup = ttk.Button(sidebar_frame, text="Signup", command=self.show_signup)
        btn_signup.pack(fill=tk.X, pady=5)
        

        btn_journal = ttk.Button(sidebar_frame, text="Journal", command=self.show_journal)
        btn_journal.pack(fill=tk.X, pady=5)

        btn_reflections = ttk.Button(sidebar_frame, text="Reflections", command=self.show_reflections)
        btn_reflections.pack(fill=tk.X, pady=5)

        # Display the initial content
        self.show_homepage()

    def show_page(self, page_class):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        page = page_class(self.content_frame)
        page.pack(fill=tk.BOTH, expand=True)

    def show_homepage(self):
        self.show_page(HomePage)

    def show_journal(self):
        self.show_page(JournalPage)

    def show_reflections(self):
        self.show_page(ReflectionsPage)
    
    def show_signup(self):
        self.show_page(SignupPage)

    def show_login(self):
        self.show_page(LoginPage)


if __name__ == "__main__":
    app = App()
    app.mainloop()
