from tkinter import *
import os


window = Tk()
window.title("Illustration and GUI")
window.geometry("500x400")
window["bg"]="black"

# iconPath = "Miniature.ico"
# if os.path.exists(iconPath):
#     window.iconbitmap(iconPath)
# else:
#     print(f"Error: the file {iconPath} does not exist")

logo = PhotoImage(file="robot.pgm")
logoimage = Label(window, image=logo)
logoimage.place(x=80, y=30, width=200, height=150)

label = Label(text="Enter your name:")
label.place(x=30, y=210, width=150, height=30)
label["bg"]="black"
label["fg"]= "white"

entryVar = StringVar()
entry_box1 = Entry(textvariable= entryVar)
entry_box1.place(x= 210 ,y=210, width=200, height=30)
entry_box1["justify"]="center"

#output box for greeting

def greet():
    name = entry_box1.get()
    output_box = Label(text="Hello" + " " + name)
    output_box.place(x=210, y=270, width=200, height=30)


button1 = Button(text="Click me", command=greet)
button1.place(x=30, y=270, width=150, height=30)



window.mainloop()