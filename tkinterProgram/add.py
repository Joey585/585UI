from tkinter import *
from tkinter import messagebox
from tmkill import tmkill_window
import webbrowser
import datetime
import os
now = datetime.datetime.now()


def newWindow():
    gui2 = Tk(className='585 Panel')
    
        
    def quitGui():
        gui2.destroy()


    def pcspecs():
        os.system('start /wait cmd /k systeminfo')

    def tmshow():
        os.system('start /wait cmd /k taskmgr')

    def show_lastRestart():
        os.system('start /wait cmd /k net statistics workstation')

    def openWebsiteWindow():

        def websiteOpener():
            if website.get():
                webbrowser.open_new_tab(website.get())
            else:
                messagebox.showerror('Error!', 'Enter website!')
        
        websiteWindow = Toplevel(gui2)
        websiteWindow.title('Website Open')
        websiteWindow.geometry('200x150')
        intro1 = Label(websiteWindow,
        text='Enter Website').pack()
        website = Entry(websiteWindow)
        website.pack()
        go = Button(
            websiteWindow,
            text='Go!',
            fg='black',
            bg='green',
            command=websiteOpener
        ).pack(pady=15)
        websiteWindow.iconbitmap(r'info.ico')



    

    intro = Label(text='Welcome, Joey585', font=("Arial", 25))
    quit = Button(
        text='Quit',
        fg='black',
        bg='red',
        command=quitGui,
    )
    time = Label(
        text=now.strftime("%m/%d/%Y, %H:%M")
    )
    websiteButton = Button(
        text='Open Website',
        fg='black',
        bg='#22e6df',
        command=openWebsiteWindow
    )
    cmdButton = Button(
        text='Get PC Specs',
        fg='black',
        bg='#33c438',
        command=pcspecs
    )
    tm_button = Button(
        text='View TM',
        fg='black',
        bg='#108fb5',
        command=tmshow
    )
    kill_tmtask = Button(
        text='Kill a TM task',
        fg='black',
        bg='#690217',
        command=tmkill_window

    )
    last_restart = Button(
        text='Work Station Statistics',
        fg='black',
        bg='#158515',
        command=show_lastRestart
    )

    # Packing
    intro.pack(side='top')
    time.pack(side='top')
    websiteButton.pack(pady=10)
    cmdButton.pack(pady=10)
    tm_button.pack(pady=10)
    kill_tmtask.pack(pady=10)
    last_restart.pack(pady=10)
    quit.pack(side='bottom', pady=15)


    gui2.geometry('500x500')
    ## gui2.iconbitmap(r'info.ico')
    ## You can make your own ico file!
    gui2.mainloop()


