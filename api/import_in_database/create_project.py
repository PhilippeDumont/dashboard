import sqlite3
import logging
from datetime import date
from database import init_database_activities_items
from methods_on_project_database import project_exist


def run(project_name):
    project_id = None
    try:
        if not project_exist.run(project_name):
            _create_new_project(project_name)
            project_id = init_database_activities_items.run(project_name)
        else:
            return None
    except Exception as err:
        logging.error(err)
    return project_id


def _create_new_project(project_name):
    conn = sqlite3.connect("api/database_files/project_db/all_project.db")
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
