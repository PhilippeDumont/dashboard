'''
Import an Item CSV file in DB
'''
import logging
import csv

from import_in_database import activity_item_import
from typing import List

def run(conn, options):
    cursor = conn.cursor()
    path = options
    _import_item_file(conn, path)
    Select = cursor.execute('SELECT * FROM items')
    cursor.close()
    return Select

def _import_item_file(conn, path):
    cursor = conn.cursor()
    _open_csv_file(cursor, path)

def _open_csv_file(cursor, path):
    '''
    Open the csv file and save the data in DB
    '''
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            activity_item_import.save_item_in_db(cursor, row)
