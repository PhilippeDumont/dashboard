'''
Import an Item CSV file in DB
'''
import logging
import csv
import sqlite3
from import_in_database import activity_item_import


def run(project_id, path):
    try:
        conn = sqlite3.connect("../database_files/act_it_db/" + str(project_id) + ".db")
        nb_items = _import_item_file(conn, path)
        conn.commit()
        # Modify the number : "nb_item" in the project database
        conn = sqlite3.connect("../database_files/project_db/all_project.db")
        cursor = conn.cursor()
        query = """UPDATE projects SET nb_items = ? WHERE id = ?"""
        cursor.execute(query, [str(nb_items), str(project_id)])
        conn.commit()
        conn.close()
    except Exception as err:
        logging.error(err)


def _import_item_file(conn, path):
    cursor = conn.cursor()
    cpt = _open_csv_file(cursor, path)
    cursor.close()
    return cpt


def _open_csv_file(cursor, path):
    '''
    Open the csv file and save the data in DB
    '''
    cpt = 0
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        try:
            for row in reader:
                cpt = cpt + 1
                activity_item_import.save_item_in_db(cursor, row)
        except Exception as exception:
            logging.error(exception)
    return cpt
