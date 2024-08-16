import tkinter as tk

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create the main window
root = tk.Tk()
root.title("Tkinter Switch Screens Example")
root.geometry("400x300")

# Create a container frame to hold the other frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create two frames for two screens
frame1 = tk.Frame(container)
frame2 = tk.Frame(container)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")

# Frame 1: Form with text boxes
label1 = tk.Label(frame1, text="This is the first screen")
label1.pack(pady=10)
entry1 = tk.Entry(frame1)
entry1.pack(pady=5)
entry2 = tk.Entry(frame1)
entry2.pack(pady=5)
button1 = tk.Button(frame1, text="Go to Next Screen", command=lambda: show_frame(frame2))
button1.pack(pady=20)

# Frame 2: New screen
label2 = tk.Label(frame2, text="This is the second screen")
label2.pack(pady=10)
button2 = tk.Button(frame2, text="Go Back to First Screen", command=lambda: show_frame(frame1))
button2.pack(pady=20)

# Show the first frame
show_frame(frame1)

# Start the main event loop
root.mainloop()
