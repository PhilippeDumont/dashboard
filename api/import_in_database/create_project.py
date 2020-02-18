import sqlite3
import logging


def run(project_name):
    try:
        create_new_project(project_name)
    except Exception as err:
        logging.error(err)


def create_new_project(project_name) :
    conn = sqlite3.connect("../database_files/project_db/all_project.db")
    cursor = conn.cursor()

    query = '''INSERT INTO projects (name) VALUES(?);'''

    try:
        cursor.execute(query, [project_name])
    except sqlite3.Error as e:
        logging.error(e.args[0])
    finally:
        cursor.close()
        conn.commit()
