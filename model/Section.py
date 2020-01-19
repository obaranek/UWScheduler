class Section:
    def __init__(self, section_number, time, prof_name, prof_rating,
                 class_number, room, course_name):
        self.__section_number = section_number
        self.__time = time #formatted time for ted's optimisation (eg: "M 14:30 - 15:30, W 14:30 - 15:20")
        self.__prof_name = prof_name
        self.__prof_rating = prof_rating
        self.__class_number = class_number
        self.__room = room
        self.__course_name = course_name


    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_course_name(self):
        return self.__course_name

    def get_section_number(self):
        return self.__section_number

    def get_time(self):
        return self.__time

    def get_starting_time(self):
        return self.__starting_time

    def get_ending_time(self):
        return self.__ending_time

    def get_prof_name(self):
        return self.__prof_name

    def get_prof_rating(self):
        return self.__prof_rating

    def get_class_number(self):
        return self.__class_number

    def get_room(self):
        return self.__room

    def get_days(self):
        return self.__days

    def set_section_number(self, section_number):
        self.__section_number = section_number

    def set_starting_time(self, starting_time):
        self.__starting_time = starting_time

    def set_ending_time(self, ending_time):
        self.__ending_time = ending_time

    def set_prof_name(self, prof_name):
        self.__prof_name = prof_name

    def set_prof_rating(self, prof_rating):
        self.__prof_rating = prof_rating

    def set_class_number(self, class_number):
        self.__class_number = class_number

    def set_room(self, room):
        self.__room = room

    def set_days(self, days):
        self.__days = days