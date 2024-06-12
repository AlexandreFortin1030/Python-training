from tkinter import *


window = Tk()
window.title("Friend Lister")
window.geometry("800x430")
window.configure(bg="black")

labelquestion = Label(text="Enter your friend's name bellow")
labelquestion.place(x=100, y=15, width=600, height=40)

entry_box = Entry(text=0)
entry_box.place(x=300, y=70, width=200, height=30)
entry_box ["justify"] = "center"

list = []
dummy_list = [] 


def add():
    global list
    global friend
    global dummy_list
    friend = entry_box.get()
    output_box1.config(text="")

    if friend:
        line_manager()
        list.append(friend)
        dummy_list.append(friend)

        output_box2.config(text=", ".join(list))

    entry_box.delete(0, END)

def reset():
    global list
    list = []
    output_box2.config(text="")
    entry_box.delete(0, END)

def line_manager():
    global dummy_list
    length = len(list)
    if len(friend) > 30:
        print("name is too long, shorten it plz")
    # make another list to store actual characters + the ones needed to go to 30
    # then mesure the length based on the new list
    elif length + len(friend) > 30 and len(dummy_list) == 0:
        number = 30 - length
        for i in range(0,number):
            dummy_list.append("/")
        list.append("\n")
    elif len(dummy_list) != 0:
        res = len(dummy_list) + len(friend)
        if res % 30 >= 30:
            list.append("\n")


button1 = Button(text="Add friend", command= add)
button1.place(x=300, y=100, width=200, height=40)

button2 = Button(text="Reset list", command= reset)
button2.place(x=300, y=150, width=200, height=40)

output_box1 = Label(text= "Name is too long shorten it please")
output_box1.place(x=200, y=205, width=400, height=30)
output_box1["bg"] = "black"
output_box1["fg"] = "red"

output_box2 = Label(text= list)
output_box2.place(x=200, y=250, width=400, height=160)
output_box2["bg"] = "orange"
output_box2["fg"] = "blue"

window.mainloop()






# Create a window that will ask the user to enter a
# name in a text box. When they click on a button it
# will add it to the end of the list that is displayed on
# the screen. Create another button which will clear
# the list.