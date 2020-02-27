import sqlite3


def run(project_name):
    conn = sqlite3.connect("../database_files/project_db/all_project.db")
    cursor = conn.cursor()
    query = "SELECT id FROM projects WHERE name=?"
    cursor.execute(query, [project_name])
    project_id = cursor.fetchone()[0]
    conn.close()
    return project_id

