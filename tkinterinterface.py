from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import messagebox
from classdatabasenotes import *
import config
import time

names_notes_name_s = 20
names_notes_dead_s = 29
names_notes_important_s = 1
names_notes_offset_s = 8
names_notes_s = names_notes_name_s + names_notes_dead_s + names_notes_important_s + names_notes_offset_s


def get_str_for_names_notes():
    list_name = base.get_list_names()
    return_string = ''
    for el in list_name:
        if len(el) > names_notes_name_s:
            return_string = return_string + el[0:names_notes_name_s] + ' | '
        else:
            return_string = return_string + el + (' ' * (names_notes_name_s - len(el))) + ' | '
        str_deadline = base.get_deadline_time(el)
        if str_deadline == 'None':
            return_string = return_string + 'Deadline None' \
                            + (' ' * (names_notes_dead_s - len('Deadline None'))) + '| '
        else:
            if str_deadline[1] == '.':
                str_deadline = '0' + str_deadline
            if str_deadline[4] == '.':
                str_deadline = str_deadline[0:3] + '0' + str_deadline[3:]
            if str_deadline[12] == ':':
                str_deadline = str_deadline[0:11] + '0' + str_deadline[11:]
            if str_deadline[15] == ':':
                str_deadline = str_deadline[0:14] + '0' + str_deadline[14:]
            if len(str_deadline) < 19:
                str_deadline = str_deadline[0:17] + '0' + str_deadline[17:]
            return_string = return_string + 'Deadline ' + str_deadline + ' | '
        if base.get_is_important(el):
            return_string = return_string + '+ \n'
        else:
            return_string = return_string + '  \n'
    return return_string


def update_names_notes():
    names_notes.delete(0.0, END)
    names_notes.insert(INSERT, get_str_for_names_notes())


def mon_to_str(mon):
    if mon == 1:
        return 'Jan'
    if mon == 2:
        return 'Feb'
    if mon == 3:
        return 'Mar'
    if mon == 4:
        return 'Apr'
    if mon == 5:
        return 'May'
    if mon == 6:
        return 'Jun'
    if mon == 7:
        return 'Jul'
    if mon == 8:
        return 'Aug'
    if mon == 9:
        return 'Sep'
    if mon == 10:
        return 'Oct'
    if mon == 11:
        return 'Nov'
    if mon == 12:
        return 'Dec'


def add_new_note():
    imp = False
    if combo.get() == 'It is important':
        imp = True
    tmp_base_info = None
    if check_base_info_state.get():
        tmp_base_info = base_info.get(0.0, END)
    # Thu Sep 27 16:42:37 2012
    if dead_line_state.get():
        deadline_str = combo_day_week.get() + ' ' + mon_to_str(mon_var.get()) + ' ' + str(day_var.get()) + ' ' + \
            str(hour_var.get()) + ':' + str(minutes_var.get()) + ':' + str(sec_var.get()) + ' ' + str(year_var.get())
        deadline_tmp_1 = time.strptime(deadline_str)
        deadline_tmp_2 = time.mktime(deadline_tmp_1)
        base.add_note(short_name_=name_new_note.get(), base_info_=tmp_base_info,
                      is_important_=imp, dead_line_=deadline_tmp_2)
    else:
        base.add_note(short_name_=name_new_note.get(), base_info_=tmp_base_info, is_important_=imp)
    update_names_notes()


def delete_note():
    check = base.delete_note(name_new_note.get())
    if check:
        update_names_notes()
        messagebox.showinfo('Delete!', name_new_note.get() + ' delete!')
    else:
        messagebox.showerror('Error delete', name_new_note.get() + ' not found!')


# Init
base = Notes(config.path_to_file)
window = Tk()
window.title('Notes')
window.geometry('930x420')
# Names notes (name(20) | deadline: 12.03.2021 00:00:00(29) | + \n)
names_notes = scrolledtext.ScrolledText(window, width=names_notes_s, height=20)
names_notes.grid(column=0, row=0)
# Name new note
name_new_note = Entry(window, width=20)
name_new_note.grid(column=0, row=1)
# Base info
base_info = Text(window, width=20, height=20)
base_info.grid(column=5, row=0)
# Important
combo = Combobox(window)
combo['values'] = ('It is important', 'It is not important')
combo.grid(column=0, row=2)
combo.current(0)
# Deadline
dead_line_state = BooleanVar()
dead_line_state.set(False)
dead_line_check = Checkbutton(window, text='Have deadline', var=dead_line_state)
dead_line_check.grid(column=0, row=3)
# Check Base Info
check_base_info_state = BooleanVar()
check_base_info_state.set(False)
check_base_info = Checkbutton(window, text='Have base info', var=check_base_info_state)
check_base_info.grid(column=0, row=4)
# Day Mon Year
lbl_d_m_y = Label(window, text='Date: ', font=('Arial Bold', 10))
lbl_d_m_y.grid(column=1, row=1)
day_var = IntVar()
mon_var = IntVar()
year_var = IntVar()
day_var.set(1)
mon_var.set(1)
year_var.set(2021)
day = Spinbox(window, from_=1, to=31, width=5, textvariable=day_var)
mon = Spinbox(window, from_=1, to=12, width=5, textvariable=mon_var)
year = Spinbox(window, from_=2021, to=2055, width=5, textvariable=year_var)
day.grid(column=2, row=1)
mon.grid(column=3, row=1)
year.grid(column=4, row=1)
combo_day_week = Combobox(window)
combo_day_week['values'] = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
combo_day_week.grid(column=5, row=1)
combo_day_week.current(0)
# Hour Min Sec
lbl_h_m_s = Label(window, text='Time: ', font=('Arial Bold', 10))
lbl_h_m_s.grid(column=1, row=3)
hour_var = IntVar()
minutes_var = IntVar()
sec_var = IntVar()
hour_var.set(0)
minutes_var.set(0)
sec_var.set(0)
hour = Spinbox(window, from_=0, to=23, width=5, textvariable=hour_var)
minutes = Spinbox(window, from_=0, to=59, width=5, textvariable=minutes_var)
sec = Spinbox(window, from_=0, to=59, width=5, textvariable=sec_var)
hour.grid(column=2, row=3)
minutes.grid(column=3, row=3)
sec.grid(column=4, row=3)
# Button Add
btn_add = Button(window, text='Add new note', command=add_new_note)
btn_add.grid(column=6, row=1)
# Button Delete
btn_delete = Button(window, text='Delete note', command=delete_note)
btn_delete.grid(column=5, row=3)


def main_tkinter():
    update_names_notes()
    window.mainloop()
    base.load()


main_tkinter()

