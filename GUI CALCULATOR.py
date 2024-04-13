from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("320x304")
window.resizable(0,0)

input_txt=StringVar()
expression=""

def click(btn):
    global expression
    expression+=str(btn)
    input_txt.set(expression)

def clear():
    global expression
    expression=""
    input_txt.set(expression)

def equal():
    global expression
    result=str(eval(expression))
    input_txt.set(result)
    expression=""

input_frame = Frame(window,height=100,width=303)
input_frame.pack()
btn_frame = Frame(window,height=220,width=303)
btn_frame.pack()

e = Entry(input_frame,width=303,font=("arial",20,"bold"),textvariable=input_txt,bd=3)
e.grid(row=0,column=0)
e.pack(ipady=30)


clr = Button(btn_frame,text="CLEAR",width=33,height=2,command=clear).grid(row=0,column=0,columnspan=3)
eq = Button(btn_frame,text="=",width=10,height=2,command=equal,bg="light grey").grid(row=5,column=4)
add = Button(btn_frame,text="+",width=10,height=2,command=lambda:click("+"),bg="light grey").grid(row=0,column=4)
sub = Button(btn_frame,text="-",width=10,height=2,command=lambda:click("-"),bg="light grey").grid(row=1,column=4)
mul = Button(btn_frame,text="*",width=10,height=2,command=lambda:click("*"),bg="light grey").grid(row=2,column=4)
div = Button(btn_frame,text="/",width=10,height=2,command=lambda:click("/"),bg="light grey").grid(row=3,column=4)


zero = Button(btn_frame,text="0",width=33,height=2,command=lambda:click(0)).grid(row=5,column=0,columnspan=3)
one = Button(btn_frame,text="1",width=10,height=2,command=lambda:click(1)).grid(row=1,column=0)
two = Button(btn_frame,text="2",width=10,height=2,command=lambda:click(2)).grid(row=1,column=1)
three = Button(btn_frame,text="3",width=10,height=2,command=lambda:click(3)).grid(row=1,column=2)
four = Button(btn_frame,text="4",width=10,height=2,command=lambda:click(4)).grid(row=2,column=0)
five = Button(btn_frame,text="5",width=10,height=2,command=lambda:click(5)).grid(row=2,column=1)
six = Button(btn_frame,text="6",width=10,height=2,command=lambda:click(6)).grid(row=2,column=2)
seven = Button(btn_frame,text="7",width=10,height=2,command=lambda:click(7)).grid(row=3,column=0)
eight = Button(btn_frame,text="8",width=10,height=2,command=lambda:click(8)).grid(row=3,column=1)
nine = Button(btn_frame,text="9",width=10,height=2,command=lambda:click(9)).grid(row=3,column=2)

