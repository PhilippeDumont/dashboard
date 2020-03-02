'''
Import an activity CSV file in the DB
'''
import logging
import csv
import sqlite3
from import_in_database import activity_item_import


def run(project_id, path):
    try:
        conn = sqlite3.connect("api/databases_files/activities_items_db/" + str(project_id) + ".db")
        nb_act = _import_activity_file(conn, path)
        conn.commit()
        # Modify the number : "nb_activities" in the project database
        conn = sqlite3.connect("api/databases_files/projects_db/all_project.db")
        cursor = conn.cursor()
        query = """UPDATE projects SET nb_activities = ? WHERE id = ?"""
        cursor.execute(query, [str(nb_act), str(project_id)])
        conn.commit()
        conn.close()
    except Exception as err:
        logging.error(err)


def _import_activity_file(conn, path):
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
        for row in reader:
            cpt = cpt + 1
            activity_item_import.save_activity_in_db(cursor, row)

    return cpt
