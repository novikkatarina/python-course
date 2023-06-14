import json
from gui import *
import csv
from database import *


def read_csv(filename):
    objects = []
    with open(filename, 'r') as file:
        for line in file:
            splitted = line.strip().split(';')
            obj = {
                "name": splitted[0],
                "surname": splitted[1],
                "description": splitted[2],
                "phone": splitted[3]

            }

            objects.append(obj)

    return objects


def read_json(filename):
    with open(filename, 'r') as f:
        result = json.loads(f.read())
        return result

    # {
    #     "name": "",
    #     "surname": "",
    #     "description": "",
    #     "phone": ''
    # }


def start():
    action = prompt()
    if action == '1':
        filename = prompt_import()
        extension = filename.split('.')[-1]
        if extension == 'csv':
            objects = read_csv(filename)
            save_data(objects)
        elif extension == 'json':
            objects = read_json(filename)
            save_data(objects)
        # read_csv(filename)
        # read data from json or csv
        # save data to database
    elif action == '2':
        extension = prompt_export()
        if extension == 'json':
            print(read_json('db.json'))
        elif extension == 'csv':
            objects = read_json('db.json')
            csv_array = []
            for obj in objects:
                csv_string = f'{obj["name"]};{obj["surname"]};{obj["description"]};{obj["phone"]}'
                csv_array.append(csv_string)

            for string in csv_array:
                print(string)



        # read data from database
        # print to console
    else:
        raise Exception('illegal action')
