'''
============================
 Python API

 It's the python API who contains the list of methods.
 To call this api you need to specifie the method and the options of this method.

================================
'''

import sys
import argparse
import sqlite3
import logging

from utils.json_conversions import to_json

from database import init_database_project
from database import init_database_activities_items
from methods_on_csv import import_activity_csv
from methods_on_csv import import_item_csv
from methods_on_project_database import get_projects, rename_project
from methods_on_project_database import get_project_with_id
from import_in_database import create_project
from methods_on_project_database import delete_project
from import_in_database import update_activity_item
from methods_on_project_database import update_project_last_opening_date

my_parser = argparse.ArgumentParser(description='Call the python API')
my_parser.add_argument('method', type=str, help='The method to call')
my_parser.add_argument('options', nargs='*', type=str, help='The options of the method called')
args = my_parser.parse_args()

input_method = args.method
input_options = args.options


list_of_function = [
    'init_db_projects',
    'create_new_project',
    'import_item_file',
    'import_activity_file',
    'get_projects'
]


try:

    if input_method == 'init_db_projects':
        print(init_database_project.run())
    elif input_method == 'create_new_project':
        print(create_project.run(input_options[0]))
    elif input_method == 'import_item_file':
        print(import_item_csv.run(input_options[0], input_options[1]))
    elif input_method == 'import_activity_file':
        print(import_activity_csv.run(input_options[0], input_options[1]))
    elif input_method == 'get_projects':
        print(to_json(get_projects.run()))
    elif input_method == 'get_project_by_id':
        print(to_json(get_project_with_id.run(input_options[0])))
    elif input_method == 'delete_project_by_id':
        print(delete_project.run(input_options[0]))
    elif input_method == 'update_project_by_id':
        print(update_activity_item.run(input_options[0], input_options[1], input_options[2]))
    elif input_method == 'update_last_opening_date_project':
        print(update_project_last_opening_date.run(input_options[0]))
    elif input_method == 'rename_project':
        print(rename_project.run(input_options[0], input_options[1]))
    else:
        print('The function ' + input_method + ' doesn\'t exist. The list of functions is: \n' + '\n'.join(list_of_function))
except IndexError as e:
    print('Add argument in the command line')
    sys.exit()
