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

# from methods import demo
# from methods import active_users
from database import init_database
from methods_on_csv import import_activity_csv
from methods_on_csv import import_item_csv
# from methods import activity

conn = sqlite3.connect('example.db')

my_parser = argparse.ArgumentParser(description='Call the python API')
my_parser.add_argument('method', type=str, help='The method to call')
my_parser.add_argument('options', nargs='?', type=str, help='The options of the method called')
args = my_parser.parse_args()
print("args: ", args)

input_method = args.method
input_options = args.options
print("options: ", input_options)


list_of_function = [
    'demo',
    'init_db',
    'activity_by_month',
    'active_users',
    'context',
    'list_activity_type',
    'list_item_type',
    'in_out_degree',
    'rush_time_mean',
    'rush_time',
    'user_month_stat',
    'user_stat',
    'import_activity_file',
    'import_item_file',
    'activities'
]


try:
    if input_method == 'init_db':
        print(init_database.run(conn))
    elif input_method == 'import-item-file':
        print(import_item_csv.run(conn, input_options))
    # elif input_method == 'active_users':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'context':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'list_activity_type':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'list_item_type':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'in_out_degree':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'rush_time_mean':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'rush_time_mean':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'rush_time':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'user_month_stat':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'user_stat':
    #     print(active_users.run(conn, input_options))
    # elif input_method == 'import_activity_file':
    #     print(import_activity_file.run(conn, input_options))
    # elif input_method == 'import_item_file':
    #     print(import_item_file.run(conn, input_options))
    # elif input_method == 'activity':
    #     print(activity.read(conn, input_options))
    else:
        print('The function ' + input_method + ' doesn\'t exist. The list of functions is: \n' + '\n'.join(list_of_function) )
except IndexError as e:
    print('Add argument in the command line')
    sys.exit()



# try:
#     if input_method == 'demo':
#         print(demo.run(input_options))
#     elif input_method == 'init_db':
#         print(init_db.run(conn, input_options))
#     elif input_method == 'activity_by_month':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'active_users':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'context':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'list_activity_type':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'list_item_type':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'in_out_degree':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'rush_time_mean':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'rush_time_mean':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'rush_time':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'user_month_stat':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'user_stat':
#         print(active_users.run(conn, input_options))
#     elif input_method == 'import_activity_file':
#         print(import_activity_file.run(conn, input_options))
#     elif input_method == 'import_item_file':
#         print(import_item_file.run(conn, input_options))
#     elif input_method == 'activity':
#         print(activity.read(conn, input_options))
#     else:
#         print('The function ' + input_method + ' doesn\'t exist. The list of functions is: \n' + '\n'.join(list_of_function) )
# except IndexError as e:
#     print('Add argument in the command line')
#     sys.exit()

