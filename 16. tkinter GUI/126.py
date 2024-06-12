from tkinter import *

window = Tk()
window.title("Count software")
window.geometry("800x300")

labelintro = Label(text="Welcome to the counting software. you can either add to the total or reset it.")
labelintro.place(x=100, y=15, width=600, height=40)

labelinfo = Label(text="Enter the amount to be added bellow")
labelinfo.place(x=200, y=50, width=400, height=30)

entry_box = Entry(text=0)
entry_box.place(x=300, y=90, width=200, height=30)
entry_box ["justify"] = "center"

labeltotal = Label(text="##################################---> Total <---###################################")
labeltotal.place(x=20, y=200, width=760, height=20)

total = 0

def add():

    count = entry_box.get()
    count = int(count)
    global total
    total = total + count
    output_box = Message(text= total)
    output_box.place(x=300, y=220, width=200, height=60)
    output_box ["justify"] = "center"
    output_box["bg"] = "orange"
    output_box["fg"] = "blue"
    entry_box.delete(0, END)


def reset():
    total = 0
    output_box = Message(text= total)
    output_box.place(x=300, y=220, width=200, height=60)
    output_box ["justify"] = "center"
    output_box["bg"] = "orange"
    output_box["fg"] = "blue"


button1 = Button(text="Add", command = add)
button1.place(x= 150, y= 140, width=100, height=30)

button2 = Button(text="Reset", command = reset)
button2.place(x=550, y=140, width=100, height=30)




window.mainloop()

















# Create a program that will ask
# the user to enter a number in a
# box. When they click on a
# button it will add that number
# to a total and display it in
# another box. This can be
# repeated as many times as
# they want and keep adding to
# the total. There should be
# another button that resets the
# total back to 0 and empties the
# original text box, ready for
# them to start again.