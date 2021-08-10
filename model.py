import csv
import json


class Person(object):

    def __init__(self, id_person=None, first_name=None, last_name=None):
        self.__id_person = id_person
        self.__first_name = first_name
        self.__last_name = last_name

    def name(self):
        return "%s %s" % (self.__first_name, self.__last_name)

    @classmethod
    def get_all(self):
        result = list()
        with open('db.txt', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                person = Person(row['id_person'], row['first_name'], row['last_name'])
                result.append(person)
                line_count += 1
        return result
