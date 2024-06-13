from tkinter import *


window = Tk()
window.title("Number Checker")
window.geometry("600x550")
window["bg"]="black"

list = Listbox(window, height=10, width=50, bg="green", font="helvetica")
list.place(x=200, y=230, width=200, height=230)


label = Label(window, text="Enter a number bellow")
label.place(x=200, y=30, width=200, height=30)
label["bg"]="black"
label["fg"]="white"

entry_box1 = Entry(window, textvariable = 0)
entry_box1.place(x=200, y=80, width=200, height=30)
entry_box1 ["justify"] = "center"


def checkNum():
    num = entry_box1.get()
    if num.isdigit():
        list.insert(END, num)
        entry_box1.delete(0, END)
    elif num.isdigit() == False:
        entry_box1.delete(0, END)


def reset():
    global list
    list.delete(0, END)
  

def save():
    tmp_list = list.get(0, END)
    with open("list.csv", "a") as file:
        for item in tmp_list:
         file.write(str(item) + "\n")

button1 = Button(window, text="Check", command=checkNum)
button1.place(x=250, y=140, width=100, height=20)

button2 = Button(window, text="Reset", command=reset)
button2.place(x=250, y=180, width=100, height=20)

button3 = Button(window, text="Save", command=save)
button3.place(x=250, y=480, width=100, height=20)


window.mainloop()



