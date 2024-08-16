import tkinter as tk
from tkinter import ttk
  
class JournalPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="This is the Journal Page")
        label.pack(pady=20)

        journalDateLabel = ttk.Label(
            font="courier",
            text="Journal Date DD/MM/YY",
            master=self
        )
        journalDateLabel.pack(fill=tk.X, pady=5)
        journalDate = ttk.Entry(self)
        journalDate.pack(fill=tk.X, pady=5)

        journalLabel = ttk.Label(
            font="courier",
            text="Journal Entry",
            master=self
        )
        journalLabel.pack(fill=tk.X, pady=5)

        journalText = tk.Text(
            master=self
        )
        journalText.pack(fill=tk.X, pady=5)