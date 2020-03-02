import sqlite3
import logging
from datetime import datetime
from database import init_database_activities_items
from methods_on_project_database import project_not_exist


def run(project_name):
    project_id = None
    try:
        # Test if the project already exist
        if project_not_exist.run(project_name):
            # Create a new project thanks to his name
            _create_new_project(project_name)
            # Create the database file for activities and items from the name of the project
            project_id = init_database_activities_items.run(project_name)
        else:
            return None
    except Exception as err:
        logging.error(err)
    return project_id


def _create_new_project(project_name):
    """
    Create a new project
    """
    conn = sqlite3.connect("api/databases_files/projects_db/all_project.db")
    cursor = conn.cursor()
    date_today = datetime.now()
    query = '''INSERT INTO projects (name,creation_date,last_opening_date,nb_activities,nb_items) VALUES(?,?,?,?,?);'''
    query_data = (project_name, date_today, date_today, 0, 0)
    try:
        cursor.execute(query, query_data)
    except sqlite3.Error as e:
        logging.error(e.args[0])
    finally:
        cursor.close()
        conn.commit()
