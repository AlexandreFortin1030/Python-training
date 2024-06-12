from tkinter import *


window = Tk()
window.title("Distance app")
window.geometry("800x300")
window.config(bg="black")

entry_var1 = StringVar()
entry_var2 = StringVar()

entry_box1 = Entry(textvariable = entry_var1)
entry_box1.place(x=150, y=100, width=200, height=30)
entry_box1 ["justify"] = "center"

label1 = Label(text="Kilometers to miles")
label1.place(x=150, y=70, width=200, height=30)
label1 ["fg"]="white"
label1 ["bg"]="black"


entry_box2 = Entry(textvariable = entry_var2)
entry_box2.place(x=450, y=100, width=200, height=30)
entry_box2 ["justify"] = "center"

label2 = Label(text="Miles to kilometers")
label2.place(x=450, y=70, width=200, height=30)
label2 ["fg"]="white"
label2 ["bg"]="black"


def convert1():
    global kilom
    global miles
    rule = 0.6214
    kilom = entry_box1.get()
    kilom = float(kilom)
    miles = kilom * rule
    miles = float(miles)
    
    output_box1 = Label(text= miles)
    output_box1.place(x=150, y= 200, width=200, height=30)
    output_box1["bg"]="orange"


def convert2():
    global kilom
    global miles
    rule = 1.6093
    miles = entry_box2.get()
    miles = float(miles)
    kilom = miles * rule
    kilom = float(kilom)
    output_box2 = Label(text= kilom)
    output_box2.place(x=450, y= 200, width=200, height=30)
    output_box2["bg"]="orange"

button1 = Button(text="Convert", command=convert1)
button1.place(x=200, y=150, width=100, height=20)


button2 = Button(text="Convert", command=convert2)
button2.place(x=500, y=150, width=100, height=20)




window.mainloop()