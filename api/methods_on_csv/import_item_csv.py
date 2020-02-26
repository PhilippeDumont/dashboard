'''
Import an Item CSV file in DB
'''
import logging
import csv
import sqlite3

from import_in_database import activity_item_import
from typing import List

from methods_on_project_database import get_project_id_with_name


def run(project_id, path):
    try:
        conn = sqlite3.connect("../database_files/act_it_db/" + str(project_id) + ".db")
        _import_item_file(conn, path)
        conn.commit()
    except Exception as err:
        logging.error(err)


def _import_item_file(conn, path):
    cursor = conn.cursor()
    _open_csv_file(cursor, path)
    cursor.close()


def _open_csv_file(cursor, path):
    '''
    Open the csv file and save the data in DB
    '''
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        try:
            for row in reader:
                activity_item_import.save_item_in_db(cursor, row)
        except Exception as exception:
            logging.error(exception)


