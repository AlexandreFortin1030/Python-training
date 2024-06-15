
from tkinter import *
import csv


window = Tk()
window.geometry("600x550")
window.title("Name and Age Tracker")
window["bg"]="black"

list = Listbox(window, height=10, width=50, bg="green", font="helvetica")
list.place(x=200, y=200, width=200, height=230)

label1 = Label(text="Enter name bellow")
label1.place(x=100, y=40, width=150, height=20)
label1["bg"]="black"
label1["fg"]="white"

label2 = Label(text="Enter age bellow")
label2.place(x=350, y=40, width=150, height=20)
label2["bg"]="black"
label2["fg"]="white"


entry_var1 = StringVar()
entry_box1 = Entry(textvariable=entry_var1)
entry_box1.place(x=100, y=70, width=150, height=30)
entry_box1["justify"]="center"

entry_var2 = StringVar()
entry_box2 = Entry(textvariable=entry_var2)
entry_box2.place(x=350, y=70, width=150, height=30)
entry_box2["justify"]="center"


# listbox pour display
# display button
# def display csv


def createFile():
    with open("131.csv", "w") as file:
        pass

def save():
    name = entry_box1.get()
    age = entry_box2.get()
    with open("131.csv", "a") as file:
        tuple = ("name: " + name + ", " + "age: " + age) + "\n"
        maintuple = ((tuple))
        file.write(maintuple)
        entry_box1.delete(0, END)
        entry_box2.delete(0, END)

def quit():
    window.destroy()

def display():
    list.delete(0, END)
    with open("131.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            list.insert(END, ', '.join(row))



button1 = Button(text="Create .csv file", command=createFile)
button1.place(x=115, y=140, width=125, height=30)

button2 = Button(text="Save", command=save)
button2.place(x=365, y=140, width=125, height=30)

button3 = Button(text="Quit", command=quit)
button3.place(x=250, y=500, width=100, height=30)
button3["bg"]="red"

button4 = Button(text="display", command=display)
button4.place(x=250, y=450, width=100, height=30)




window.mainloop()


