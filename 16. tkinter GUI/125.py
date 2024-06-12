from tkinter import *
import random



window = Tk()
window.title("Throw a dice")
window.geometry("400x100")



def click():
    num = random.randint(0, 6)
    output_box = Message(text = num)
    output_box.place(x=170, y=70, width=70, height=30)


button1 = Button(text="Throw", command = click)
button1.place(x=150, y=30, width=100, height=30)

window.mainloop()


# Write a program that
# can be used instead
# of rolling a six-sided
# dice in a board game.
# When the user clicks
# a button it should
# display a random
# whole number
# between 1 to 6
# (inclusive).