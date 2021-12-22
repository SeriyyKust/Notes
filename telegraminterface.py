import telebot
from telebot import types
import config
from classdatabasenotes import*

bot = telebot.TeleBot(config.token)
base = Notes(config.path_to_file)
help_string = "\start: to start bot\n" \
              "\help: to show commands\n" \
              "\shownotes: to show all notes\n" \
              "\modenotes: to change database of notes"
names_notes_name_s = 20
names_notes_dead_s = 29
names_notes_important_s = 1
names_notes_offset_s = 8
names_notes_s = names_notes_name_s + names_notes_dead_s + names_notes_important_s + names_notes_offset_s
_markup = False


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


def is_name_of_notes(name):
    names = base.get_list_names()
    for _name in names:
        if name == _name:
            return True
    return False


def get_str_info(name):
    str_ = 'name: ' + name + '\n' + 'info: ' + base.get_info_string(name) + '\n'
    str_ = str_ + 'start: ' + base.get_start_time(name) + '\n'
    dead = base.get_deadline_time(name)
    if dead is not None:
        str_ = str_ + 'Deadline: ' + dead + '\n'
    important = base.get_is_important(name)
    if important:
        str_ = str_ + 'It is important' + '\n'
    return str_


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id, 'Hi, I\'m Notes_bot.')


@bot.message_handler(commands=['help'])
def send_help_message(message):
    bot.send_message(message.chat.id, help_string)


@bot.message_handler(commands=['shownotes'])
def show_all_notes(message):
    bot.send_message(message.chat.id, get_str_for_names_notes())


@bot.message_handler(commands=['showone'])
def show_one(message):
    global _markup
    names = base.get_list_names()
    list_item = []
    markup = types.ReplyKeyboardMarkup()
    for el in names:
        itembtn = types.KeyboardButton(el)
        list_item.append(itembtn)
    for item in list_item:
        markup.row(item)
    bot.send_message(message.chat.id, 'Choose the note: ', reply_markup=markup)
    _markup = True


@bot.message_handler(content_types=['text'])
def check_text(message):
    global _markup
    if is_name_of_notes(message.text):
        if _markup is True:
            keyboard_delete = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, get_str_info(message.text), reply_markup=keyboard_delete)
            _markup = False
        else:
            bot.send_message(message.chat.id, get_str_info(message.text))


bot.infinity_polling()