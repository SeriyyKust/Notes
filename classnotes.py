import time


class Note:

    def __init__(self, short_name_, base_info_=None, is_important_=False, dead_line_=None):
        self.short_name = short_name_
        self.base_info = base_info_
        self.start_time = time.time()
        self.is_important = is_important_
        self.dead_line = dead_line_

    def is_equal(self, other_note):
        if self.dead_line == other_note.dead_line:
            return True
        else:
            return False

    def is_more(self, other_note):
        if self.dead_line is not None:
            if other_note is not None:
                if self.dead_line > other_note.dead_line:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if other_note is not None:
                return True
            else:
                return False

    def is_less(self, other_note):
        if self.dead_line is not None:
            if other_note is not None:
                if self.dead_line < other_note.dead_line:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def __lt__(self, other):
        return self.is_less(other)

    def __gt__(self, other):
        return self.is_more(other)

    def __eq__(self, other):
        return self.is_equal(other)

    def change(self, name=None, base_info=None, dead_line=None, is_important=None):
        if name is not None:
            self.short_name = name
        if base_info is not None:
            self.base_info = base_info
        if dead_line is not None:
            self.dead_line = dead_line
        if is_important is not None:
            if is_important is not False and is_important is not True:
                return False
            else:
                self.is_important = is_important
        return True

    def get_name(self):
        return self.short_name

    def get_base_info(self):
        return self.base_info

    def get_is_important(self):
        return self.is_important

    def start_time_to_string(self):
        struct_t = time.gmtime(self.start_time)
        return_string = str(struct_t.tm_mday) + ' ' + str(struct_t.tm_mon) + ' ' + str(struct_t.tm_year) + \
            str(' ') + str((struct_t.tm_hour + 3) % 24) + ':' + str(struct_t.tm_min) + ':' + str(struct_t.tm_sec)
        return return_string

    def deadline_time_to_string(self):
        if self.dead_line is None:
            return 'None'
        struct_t = time.gmtime(self.dead_line)
        return_string = str(struct_t.tm_mday) + ' ' + str(struct_t.tm_mon) + ' ' + str(struct_t.tm_year) + \
            str(' ') + str((struct_t.tm_hour + 3) % 24) + ':' + str(struct_t.tm_min) + ':' + str(struct_t.tm_sec)
        return return_string

    def __str__(self):
        return_string = self.short_name  + '\n' + \
            'start: ' + self.start_time_to_string() + '\n' + \
            'deadline: ' + self.deadline_time_to_string() + '\n'
        if self.base_info is not None:
            return_string = return_string + 'Info: ' + self.base_info + '\n'
        if self.is_important:
            return_string = return_string + 'This is important' + '\n'
        else:
            return_string = return_string + 'This isn\'t important' + '\n'
        return return_string

    def __del__(self):
        pass

