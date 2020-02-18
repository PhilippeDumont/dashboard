import sqlite3
import logging
from datetime import date


def run(project_name):
    try:
        _create_new_project(project_name)
    except Exception as err:
        logging.error(err)


def _create_new_project(project_name):
    conn = sqlite3.connect("../database_files/project_db/all_project.db")
    cursor = conn.cursor()
    date_today = date.today().isoformat()
    query = '''INSERT INTO projects (name, creation_date, last_opening_date, nb_activities, nb_items) VALUES(?,?,?,?,?);'''
    query_data = (project_name, date_today, date_today, 0, 0)
    try:
        cursor.execute(query, query_data)
    except sqlite3.Error as e:
        logging.error(e.args[0])
    finally:
        cursor.close()
        conn.commit()
