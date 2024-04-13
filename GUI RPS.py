from tkinter import *
import random

window = Tk()
window.geometry("345x300")
window.title("Rock Paper Scissors")
window.resizable(0, 0)

computer_value = {"0": "Rock", "1": "Paper", "2": "Scissor"}

def reset():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    button_disable()

def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=c_v)
    button_disable()

def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Scissor")
    l3.config(text=c_v)
    button_disable()

Label(window, text="ROCK PAPER SCISSORS", font=("arial", 20, "bold")).grid(row=0, column=0, columnspan=3, pady=20)

l1 = Label(window, text="Player", font=("arial", 15, "bold"))
l1.grid(row=1, column=0)
l2 = Label(window, text="VS", font=("arial", 15, "bold"))
l2.grid(row=1, column=1)
l3 = Label(window, text="Computer", font=("arial", 15, "bold"))
l3.grid(row=1, column=2)
l4 = Label(window, text="", font=("arial", 15, "bold"), relief="solid", width=25)
l4.grid(row=3, column=0, columnspan=3, pady=20)

b1 = Button(window, text="Rock", font=("arial", 8, "bold"), width=10, command=isrock)
b1.grid(row=4, column=0)
b2 = Button(window, text="Paper", font=("arial", 8, "bold"), width=10, command=ispaper)
b2.grid(row=4, column=1)
b3 = Button(window, text="Scissor", font=("arial", 8, "bold"), width=10, command=isscissor)
b3.grid(row=4, column=2)
b4 = Button(window, text="Reset", font=("arial", 15, "bold"), width=20, fg="red", command=reset)
b4.grid(row=5, column=0, columnspan=3, pady=20)

window.mainloop()
