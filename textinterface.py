import config
import time
from classdatabasenotes import *


def Add_Note():
    global base
    name = input('Enter name: ')
    check = int(input('Addition information? (1 - yes, 2 - no): '))
    if check == 1:
        base_info = None
        check = int(input('Enter info? (1 - yes, 2 - no): '))
        if check == 1:
            base_info = input('Enter info: ')
        check = int(input('It is important? (1 - yes, 2 - no): '))
        if check == 1:
            is_important = True
        else:
            is_important = False
        check = int(input('Enter deadline? (1 - yes, 2 - no): '))
        if check == 1:
            str_deadline = input('Enter deadline:(Thu Sep 27 16:42:37 2012): ')
            dead_struct = time.strptime(str_deadline)
            dead_c = time.mktime(dead_struct)
            base.add_note(name, base_info_=base_info, is_important_=is_important, dead_line_=dead_c)
        else:
            base.add_note(name, base_info_=base_info, is_important_=is_important)
    else:
        base.add_note(name)

def Delete_Note():
    global base
    name = input('Enter name: ')
    if base.delete_note(name):
        print(name + ' delete!')
    else:
        print(name + 'not found!')

def Show_Info():
    names = base.get_list_names()
    if len(names) == 0:
        print('List is empty')
    else:
        for n in names:
            print(base.get_info_string(n))


def Menu():
    print('1) Show info')
    print('2) Add new note')
    print('3) Delete note')
    print('0) Exit')


base = Notes(config.path_to_file)
c = 1
while c != 0:
    Menu()
    c = int(input('Enter: '))
    if c == 2:
        Add_Note()
    elif c == 1:
        Show_Info()
    elif c == 3:
        Delete_Note()
    else:
        pass
base.load()