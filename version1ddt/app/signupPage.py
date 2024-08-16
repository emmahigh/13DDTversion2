import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
  
class SignupPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Username label and entry
        self.label_username = tk.Label(self, text="Username")
        self.label_username.pack(pady=5)
        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        # Password label and entry
        self.label_password = tk.Label(self, text="Password")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        # Signup button
        self.btn_signup = tk.Button(self, text="Signup", command=self.signup)
        self.btn_signup.pack(pady=20)
    
    # Function to save user data
    def signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if username and password:
            conn = sqlite3.connect('./app/database/database.db')
            cursor = conn.cursor()
            
            try:
                cursor.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
                ''', (username, password))
                conn.commit()
                messagebox.showinfo("Success", "Signup successful! please login")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")
            finally:
                conn.close()
        else:
            messagebox.showerror("Error", "Please enter both username and password")


        