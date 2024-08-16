from tkinter import *
from tkinter import messagebox
import journal
import homepage
import reflections

def show_frame(frame):
    frame.tkraise()

def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1 , font="courier" , command = login_verify).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if username1 == "emma":
        if password1 in "emma1":
            login_screen.destroy()

        else:
            user_not_found()

    else:
        user_not_found()
        

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=remove_user_mot_found).pack()

def remove_user_mot_found():
    user_not_found_screen.destroy()


root = Tk()
root.iconbitmap('')
root.geometry("1100x700")

# Create a container frame to hold the other frames
container = Frame(root)
container.pack(fill="both", expand=True)

menuFrame = Frame(container, width=200, bg='lightgray')
menuFrame.pack(side="top", fill="y")

contentFrame = Frame(container)
contentFrame.pack(side="bottom", fill="both", expand=True)

#setup the journal frame
journal.setup(menuFrame, contentFrame)
homepage.setup(menuFrame, contentFrame)
reflections.setup(menuFrame, contentFrame)

""" reflections = Button( 
    text="Reflections",
    bg="white",
    fg="black",
    font="courier" ,
    width=15,
    height=10,
    master=menuFrame,
    anchor=CENTER

)
reflections.grid(row =0, column=2, padx=2) 
 """
moodtracker = Button(
    text="Mood Tracker",
    bg="white",
    fg="black",
    font="courier" ,
    width=15,
    height=10,
    master=menuFrame,
    anchor=CENTER
)
moodtracker.grid(row =0, column=3, padx=2)

mealplanning  = Button( 
    text="Meal Planning",
    bg="white",
    fg="black",
    font="courier" ,
    width=15,
    height=10,
    master=menuFrame,
    anchor=CENTER

)
mealplanning.grid(row =0, column=4, padx=2)

    
loginsignup = Button( 
    text="Login",
    bg="white",
    fg="black",
    width=15,
    height=10,
    master=menuFrame,
    anchor=CENTER,
    command=login
)
loginsignup.grid(row =0, column=5, padx=2)

show_frame(homepage.homePageFrame)

root.mainloop()

