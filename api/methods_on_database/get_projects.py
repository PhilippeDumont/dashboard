'''
return the list of project in database
'''
import sqlite3
import logging


def run():
    try:
        conn = sqlite3.connect('../database_files/project_db/all_project.db')

        conn.commit()
    except Exception as err:
        logging.error("There is no project ... Yet")