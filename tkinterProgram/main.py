from tkinter import * 
from tkinter import messagebox
from add import *
import time

gui = Tk(className='585 Application')

def showMsg():
    if username.get() == 'Joey585' and password.get() == 'test':
        gui.destroy()
        newWindow()
    else:
        messagebox.showerror('Error!', 'Invalid Login!')

def closeGui():
    gui.destroy()
    

button = Button(gui, 
    text='Submit',
    bg='yellow',
    fg='black',
    command=showMsg
)
button2 = Button(
    text='Quit',
    bg='red',
    fg='black',
    command=closeGui
)
signin = Label(text='Sign in!', font=('Arial', 25))
intro = Label(text='Enter Username:')
introPass = Label(text='Enter password')
username = Entry()
usernameGet = username.get()
password = Entry(show='*')


# Packing
signin.pack(side='top')
intro.pack()
username.pack()
introPass.pack()
password.pack()
button.pack(pady=20)
button2.pack(side='bottom', pady=15)


gui.geometry("500x500")
gui.iconbitmap(r'info.ico')

gui.mainloop()