from tkinter import *
import random

num1 = random.randint(10, 50)
num2 = random.randint(10, 50)

window = Tk()
window.title("Math quiz")
window.geometry("600x500")
window["bg"]="black"

label1 = Label(text="Add these two numbers")
label1.place(x=200, y=30, width=200, height=30)
label1["bg"]= "black"
label1["fg"]="white"

label2 = Label(text= num1)
label2.place(x=85, y=80, width=150, height=30)
label2["bg"]= "black"
label2["fg"]="white"

labelAdd = Label(text= " + ")
labelAdd.place(x=290, y=80, width=30, height=30)
labelAdd["bg"]= "black"
labelAdd["fg"]="white"
labelAdd["justify"]="center"

label3 = Label(text= num2)
label3.place(x=340, y=80, width=200, height=30)
label3["bg"]= "black"
label3["fg"]="white"

labelequal = Label(text="Enter result:")
labelequal.place(x=260, y=150, width=80, height=30)
labelequal["bg"]= "black"
labelequal["fg"]="white"


entryVar = StringVar()
entry_box= Entry(textvariable= entryVar)
entry_box.place(x=250, y=200, width=100, height=30)
entry_box["justify"]="center"

logoimage = Label(window)
logoimage.place(x=200, y=320, width=200, height=150)
logoimage["bg"]="black"

true_logo = None
false_logo = None

entry_box.focus()

def changeNum():
    global num1, num2
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    label2.config(text=num1)
    label3.config(text=num2)

def clearInput():
    entry_box.delete(0, END)


def check(event=None):                                            # event = None, pas très clair...
    global true_logo, false_logo
    res = num1 + num2
    proposal = entry_box.get()

    if int(proposal) == res:
        true_logo = PhotoImage(file="true.gif")
        logoimage.config(image=true_logo)
        logoimage.image = true_logo
        
    
    else:
        false_logo = PhotoImage(file="false.gif")
        logoimage.config(image=false_logo)                         # Pourquoi des étapes avec config puis nouvelles référence à l'image ensuite??
        logoimage.image = false_logo
    
    changeNum()
    clearInput()
    entry_box.focus()

button1= Button(text="Check", command=check)
button1.place(x=250, y=260, width=100, height=30)

window.bind('<Return>', check)

window.mainloop()
