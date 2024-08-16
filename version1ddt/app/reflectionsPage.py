import tkinter as tk
from tkinter import ttk
  
class ReflectionsPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="This is the Reflections Page")
        label.pack(pady=20)

        reflectionsDateLabel = ttk.Label(
            font="courier",
            text="Reflections Date DD/MM/YY",
            master=self
        )
        reflectionsDateLabel.pack(fill=tk.X, pady=5)
        reflectionsDate = ttk.Entry(self)
        reflectionsDate.pack(fill=tk.X, pady=5)

        reflectionsLabel = ttk.Label(
            font="courier",
            text="Reflections Entry",
            master=self
        )
        reflectionsLabel.pack(fill=tk.X, pady=5)
        
        promptLabel = ttk.Label(
            font="courier",
            text="Today I am grafeful for...",
            master=self
        )
        promptLabel.pack(fill=tk.X, pady=5)

        reflectionsText = tk.Text(
            master=self
        )
        reflectionsText.pack(fill=tk.X, pady=5)
       
        prompt1Label = ttk.Label(
            font="courier",
            text="MY high of today was...",
            master=self
        )
        prompt1Label.pack(fill=tk.X, pady=5)

        reflectionsText = tk.Text(
            master=self
        )
        reflectionsText.pack(fill=tk.X, pady=5)
        
        prompt1Label = ttk.Label(
            font="courier",
            text="MY low of today was...",
            master=self
        )
        prompt1Label.pack(fill=tk.X, pady=5)

        reflectionsText = tk.Text(
            master=self
        )
        reflectionsText.pack(fill=tk.X, pady=5)

        prompt1Label = ttk.Label(
            font="courier",
            text="What are my plans for tomorrow...",
            master=self
        )
        prompt1Label.pack(fill=tk.X, pady=5)

        reflectionsText = tk.Text(
            master=self
        )
        reflectionsText.pack(fill=tk.X, pady=5)