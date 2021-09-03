from tkinter import *
from tkinter import messagebox
import webbrowser
import datetime
now = datetime.datetime.now()


def newWindow():
    gui2 = Tk(className='585 Panel')
    
        
    def quitGui():
        gui2.destroy()

    def openWebsiteWindow():

        def websiteOpener():
            if website.get():
                webbrowser.open_new_tab(website.get())
            else:
                messagebox.showerror('Error!', 'Enter website!')
        
        websiteWindow = Toplevel(gui2)
        websiteWindow.title('Website Open')
        websiteWindow.geometry('200x200')
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
        ).pack()



    

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
        bg='blue',
        command=openWebsiteWindow
    )

    # Packing
    intro.pack(side='top')
    time.pack(side='top')
    websiteButton.pack()
    quit.pack(side='bottom')


    gui2.geometry('500x500')
    gui2.iconbitmap(r'info.ico')
    gui2.mainloop()

