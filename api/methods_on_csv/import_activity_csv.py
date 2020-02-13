'''
Import an Activity CSV file in DB
'''
import csv
from import_in_database import activity_item_import


def run(conn, option):
    cursor = conn.cursor()
    path = option
    _import_activity_file(conn, path)
    cursor.execute('SELECT * FROM activities')
    return cursor.fetchone()


def _import_activity_file(conn, path):
    cursor = conn.cursor()
    _open_csv_file(cursor, path)


def _open_csv_file(cursor, path):
    '''
    Open the csv file and save data in DB
    '''
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            activity_item_import.save_activity_in_db(cursor, row)

