from classnotes import Note
import os
import pickle


class Notes:
    def __init__(self, path):
        self.list_notes = []
        self.list_index = dict()
        self.count_notes = 0
        self.path_to_file = path
        try:
            file = open(path, 'rb')
        except IOError as e:
            print('File \'' + str(path) + '\' not found!')
        else:
            with file:
                file.seek(0, os.SEEK_END)
                if file.tell():
                    file.seek(0, 0)
                    self.list_notes = pickle.load(file)
                    for element in self.list_notes:
                        self.list_index[element.get_name()] = self.count_notes
                        self.count_notes += 1

    def add_note(self, short_name_, base_info_=None, is_important_=False, dead_line_=None):
        n = Note(short_name_, base_info_, is_important_, dead_line_)
        self.list_notes.append(n)
        self.list_index[short_name_] = self.count_notes
        self.count_notes += 1
        return True

    def delete_note(self, name):
        index = self.list_index.get(name)
        if index is None:
            return False
        else:
            self.list_notes[index], self.list_notes[self.count_notes - 1] = self.list_notes[self.count_notes - 1], self.list_notes[index]
            name_tmp = self.list_notes[index].get_name()
            self.list_index[name_tmp] = index
            n = self.list_notes.pop()
            self.count_notes -= 1
            self.list_index.pop(name)
            n.__del__()
            return True

    def get_count(self):
        return self.count_notes

    def get_list_names(self):
        list_name = []
        for element in self.list_notes:
            list_name.append(element.get_name())
        return list_name

    def get_deadline_time(self, name):
        index = self.list_index.get(name)
        if index is None:
            return None
        return self.list_notes[index].deadline_time_to_string()

    def get_start_time(self, name):
        index = self.list_index.get(name)
        if index is None:
            return None
        return self.list_notes[index].start_time_to_string()

    def get_is_important(self, name):
        index = self.list_index.get(name)
        if index is None:
            return None
        return self.list_notes[index].get_is_important()

    # this will be delete
    def get_info_string(self, name):
        index = self.list_index.get(name)
        if index is None:
            return 'None'
        else:
            return str(self.list_notes[index])

    def load(self):
        with open(self.path_to_file,'wb') as file:
            pickle.dump(self.list_notes, file)

    def __del__(self):
        pass


