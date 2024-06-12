from tkinter import *


window = Tk()
window.title("Number Checker")
window.geometry("600x300")
window["bg"]="black"

entry_var1 = StringVar()

label = Label(text="Enter a number bellow")
label.place(x=200, y=30, width=200, height=30)
label["bg"]="black"
label["fg"]="white"

entry_box1 = Entry(textvariable = entry_var1)
entry_box1.place(x=200, y=80, width=200, height=30)
entry_box1 ["justify"] = "center"

def checkNum():
    global list
    num = entry_var1.get()
    if num.isdigit():
        list.append(num)
    else:
        entry_box1.delete(0,END)

def reset():
    global list
    list = []

def display():
    output_box= Label(text=list)
    output_box.place(x=100, y=50, width=400, height=100)
    output_box["bg"]="black"
    output_box["fg"]="white"


button1 = Button(text="Check", command=checkNum)
button1.place(x=250, y=140, width=100, height=20)

list = Listbox()
list.place()

button2 = Button(text="reset", command=reset)
button2.place(x=250, y=180, width=100, height=20)

window.mainloop()




# Create a window that will ask the
# user to enter a number in a text box.
# When they click on a button it will
# use the code
# variable.isdigit() to check
# to see if it is a whole number. If it is
# a whole number, add it to a list box,
# otherwise clear the entry box. Add
# another button that will clear the
# list.