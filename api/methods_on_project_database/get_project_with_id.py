import sqlite3
import logging
from model.project_model import Project


def run(project_id):
    try:
        conn = sqlite3.connect('../database_files/project_db/all_project.db')
        project = _get_project(conn, project_id)
        conn.commit()
        conn.close()
        return project
    except Exception as err:
        logging.error(err)


def _get_project(conn, project_id):
    cursor = conn.cursor()
    query = "SELECT * FROM projects WHERE id = ?"
    cursor.execute(query, str(project_id))
    row = cursor.fetchone()
    project = Project(row[0], row[1], row[2], row[3], row[4], row[5])
    return project