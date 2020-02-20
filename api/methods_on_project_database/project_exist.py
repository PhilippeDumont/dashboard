import sqlite3


def run(project_name):
    conn = sqlite3.connect("api/database_files/project_db/all_project.db")
    cursor = conn.cursor()
    query = ("SELECT * FROM  projects WHERE name=?")
    cursor.execute(query,project_name)
    test = cursor.fetchall()
    if test is None:
        return False
    else:
        return True
