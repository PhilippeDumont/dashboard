"""
Search the database for the project IF it exist
"""
import sqlite3


def run(project_name):
    conn = sqlite3.connect("../databases_files/projects_db/all_project.db")
    cursor = conn.cursor()
    query = ("SELECT * FROM  projects WHERE name=?")
    cursor.execute(query,[project_name])
    test = cursor.fetchall()
    if len(test) == 0:
        return True
    else:
        return False
