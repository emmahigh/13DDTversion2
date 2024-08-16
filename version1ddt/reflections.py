from tkinter import *
from tkinter import messagebox

def showreflections():
    reflectionsPageFrame.tkraise()

def setup(menuFrame, contentFrame):

    global reflectionsPageFrame,reflectionsText
    reflectionsPageFrame = Frame(master=contentFrame)
    reflectionsPageFrame.grid(row = 0, column = 0, rowspan = 3, columnspan = 8, sticky="nsew")

    reflections = Button(
       text="Reflections",
       bg="white",
       fg="black",
       font="courier" ,
       width=15,
       height=10,
       master=menuFrame,
       anchor=CENTER,
       command=showreflections
    )
    reflections.grid(row =0, column=2, padx=2)
   
    reflectionsDateLabel = Label(
        bg="white",
        fg="black",
        font="courier",
        text="reflections Date DD/MM/YY",
        master=reflectionsPageFrame
    )
    reflectionsDateLabel.grid(row=0, column=0,columnspan=8)
    reflectionsDate = Entry(reflectionsPageFrame)
    reflectionsDate.grid(row=2, column=0,columnspan=8)

    reflectionsLabel = Label(
        bg="white",
        fg="black",
        font="courier",
        text="reflections Entry",
        master=reflectionsPageFrame
    )
    reflectionsLabel.grid(row=3, column=0,columnspan=8)

    reflectionsText = Text(
        master=reflectionsPageFrame
    )
    reflectionsText.grid(row=4, column=0,columnspan=8)
