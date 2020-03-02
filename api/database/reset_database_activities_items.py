"""
Reset the database by deleting all the data in the tables activities and items
"""
import sqlite3


def run(project_id):
    conn = sqlite3.connect("api/databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    _reset_database(cursor)
    cursor.close()
    conn.commit()


def _reset_database(cursor):
    cursor.execute('DELETE FROM activities')
    cursor.execute('DELETE FROM items')
