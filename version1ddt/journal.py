from tkinter import *
from tkinter import messagebox

def showJournal():
    journalPageFrame.tkraise()

def setup(menuFrame, contentFrame):

    global journalPageFrame,journalText
    journalPageFrame = Frame(master=contentFrame)
    journalPageFrame.grid(row = 0, column = 0, rowspan = 2, columnspan = 7, sticky="nsew")

    journal = Button(
        text="Journal",
        bg="white",
        fg="black",
        font="courier" ,
        width=15,
        height=10,
        master=menuFrame,
        anchor=CENTER,
        command=showJournal
    )
    journal.grid(row=0, column=1, padx=2)

    journalDateLabel = Label(
        bg="white",
        fg="black",
        font="courier",
        text="Journal Date DD/MM/YY",
        master=journalPageFrame
    )
    journalDateLabel.grid(row=0, column=0,columnspan=7)
    journalDate = Entry(journalPageFrame)
    journalDate.grid(row=1, column=0,columnspan=7)

    journalLabel = Label(
        bg="white",
        fg="black",
        font="courier",
        text="Journal Entry",
        master=journalPageFrame
    )
    journalLabel.grid(row=2, column=0,columnspan=7)

    journalText = Text(
        master=journalPageFrame
    )
    journalText.grid(row=3, column=0,columnspan=7)
