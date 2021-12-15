from tkinter import *
from tkinter.ttk import *
from classdatabasenotes import *
import config


def get_str_names():
    global base
    list_name = base.get_list_names()
    return_string = ''
    for el in list_name:
        return_string = return_string + el + '\n'
    return return_string


def add_new_note():
    global base
    imp = False
    if combo.get() == 'It is important':
        imp = True
    base.add_note(short_name_=namenewnote.get(), is_important_=imp)
    lbl.configure(text=get_str_names())


base = Notes(config.path_to_file)


window = Tk()
window.title('Notes')
window.geometry('400x250')


lbl = Label(window, text=get_str_names(), font=('Arial Bold', 25))
lbl.grid(column=0, row=0)


namenewnote = Entry(window, width=20)
namenewnote.grid(column=1, row=0)


btn = Button(window, text='Add new note', command=add_new_note)
#btn = Button(window, text='Add new note', bg="black", fg="red")
btn.grid(column=1, row=1)

combo = Combobox(window)
combo['values'] = ('It is important', 'It is not important')
combo.grid(column=1, row=2)
combo.current(0)

window.mainloop()

base.load()