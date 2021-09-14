from tkinter import *
from tkinter import messagebox
import os

def tmkill_window():

    tmkill = Tk(className='TM kill')

    def tmKillProccess():
        if process.get():
            os.system('start /wait cmd /k taskkill /im {} /f'.format(process.get()))
        else:
            messagebox.showerror('Error!', 'Please enter proccess!')


    process = Entry(tmkill)
    submit = Button(
        tmkill,
        text='Kill',
        fg='black',
        bg='red',
        command=tmKillProccess
    )
    
    process.pack()
    submit.pack(pady=15, side='bottom')



    tmkill.geometry('200x150')
    tmkill.iconbitmap(r'info.ico')
    tmkill.mainloop()