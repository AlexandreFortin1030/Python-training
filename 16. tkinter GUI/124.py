from tkinter import *

# Static

window = Tk()
window.title("My first window")
window.geometry("600x200")

label = Label(text = "Enter your name")
label.place(x=200, y=20, width=200, height=25)

entry_box = Entry(text = 0)
entry_box.place(x=180, y=40, width=240, height= 30)
entry_box ["justify"] = "center"

# Dynamic

def Click():
    name = entry_box.get()
    output_box = Message(text= "Hello " + name )
    output_box.place(x=200, y=120, width=200, height=40)
    output_box ["justify"] = "center"
    output_box["bg"] = "orange"
    output_box["fg"] = "blue"

    # msg = Label(window, text= "Hello00" + name)
    # msg.place(x=250, y=120, width=100, height=30)
    # msg["bg"] = "orange"
    # msg["fg"] = "blue"

button1 = Button(text="Click here", command = Click)
button1.place(x=250, y=80, width=100, height=30)

window.mainloop()








# Create a window that will
# ask the user to enter their
# name.
# When they click on
# a button it should display
# the message “Hello” and
# their name and change
# the background colour
# and font colour of the
# message box.