from tkinter import *
import tkinter.scrolledtext
import tkinter.filedialog
import tkinter.messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askokcancel
# creates the text area
root = tkinter.Tk(className='A text editor')
textPad = tkinter.scrolledtext.ScrolledText(root, width=100, height=80)


# creates a menu


def open_command():
    file = tkinter.filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file is not None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()


def save_command():
    file = tkinter.filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file is not None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()


def exit_command():
    if tkinter.messagebox.askokcancel('Quit', 'Do you really want to quit?'):
        root.destroy()


def about_command():
    label = tkinter.messagebox.showinfo('About', 'A text pad \n Not even copyrighted \n No rights :(')


def dummy():
    menu = Menu(root)
    root.config(menu=menu)
    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label='New', command=new_command)
    file_menu.add_command(label='Open', command=open_command)
    file_menu.add_command(label='Save', command=save_command)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=exit_command)
    help_menu = Menu(menu)
    menu.add_cascade(label='Help', menu=help_menu)
    help_menu.add_command(label='About...', command=about_command)
#end of the menu creation
dummy()

textPad.pack()
root.mainloop()
