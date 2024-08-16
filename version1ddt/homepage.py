from tkinter import *
from tkinter import messagebox

def setup(menuFrame, contentFrame):

    global homePageFrame, homepageImg, logoresize

    homePageFrame = Frame(master=contentFrame)
    homePageFrame.grid(row = 0, column = 0, rowspan = 2, columnspan = 7, sticky="nsew")

    homepageImg = PhotoImage(file="./img/homescreen.png")
    homepage = Label(master=homePageFrame, image=homepageImg)
    homepage.grid(row=1, column=0,columnspan=7)
    
    logoImg = PhotoImage(file="./img/logo.png")
    logoresize=logoImg.subsample(6,6)
    logo = Button(
        text="Logo",
        bg="white",
        fg="black",
        font="courier" ,
        master=menuFrame,
        anchor=CENTER,
        image=logoresize,
        command=homePageFrame.tkraise()
    )
    logo.grid(row =0, column=0, padx=2)

