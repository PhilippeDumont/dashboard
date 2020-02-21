'''
return the list of project in database
'''
import sqlite3
import logging

from model.project_model import Project


def run():
    try:
        conn = sqlite3.connect('api/database_files/project_db/all_project.db')
        all_projects = _get_all_projects(conn)
        conn.commit()
        conn.close()
        return all_projects
    except Exception as err:
        logging.error(err)


def _get_all_projects(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    list_projects = list()
    for row in cursor:
        project_temp = Project(row[0], row[1], row[2], row[3], row[4], row[5])
        list_projects.append(project_temp)
    cursor.close()
    return list_projects
