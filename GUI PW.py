from tkinter import *
import random
import string

window = Tk()
window.geometry("290x300")
window.title("Password Generator")
window.resizable(0, 0)


def generate_password():
    
    password_length = int(l1.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    l2.config(text=password)

Label(window, text="Password Length", font=("arial", 20, "bold")).grid(row=0, column=0)
l1 = Spinbox(window, from_=4, to_=32, font=("arial", 15, "bold"))
l1.grid(row=1, column=0, padx=10, pady=20)

b = Button(window, text="Generate Password", font=("arial", 15, "bold"), command=generate_password)
b.grid(row=2, column=0, pady=20)

l2 = Label(window, text="", font=("arial", 20, "bold"), relief="solid", width=15)
l2.grid(row=3, column=0, pady=20, padx=10)

window.mainloop()
