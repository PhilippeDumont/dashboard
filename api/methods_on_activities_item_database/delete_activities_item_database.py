import os
import sqlite3


def run(project_id):
    os.remove("api/database_files/act_it_db/" + str(project_id) + ".db")
    conn = sqlite3.connect("api/database_files/project_db/all_project.db")
    cursor = conn.cursor()
    query = "DELETE FROM projects WHERE id = ?"
    cursor.execute(query, project_id)
    conn.commit()
    conn.close()
