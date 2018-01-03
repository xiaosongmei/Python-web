#! /usr/bin/python3


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male':
            self.__gender = gender
        elif gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('error')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('test error')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('test error')
    else:
        print('succesful')
