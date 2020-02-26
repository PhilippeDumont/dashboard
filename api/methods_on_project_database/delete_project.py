import sqlite3

from methods_on_activities_item_database import delete_activities_item_database


def run(project_id):
    delete_activities_item_database.run(project_id)
    conn = sqlite3.connect("../database_files/project_db/all_project.db")
    cursor = conn.cursor()
    query = "DELETE FROM projects WHERE id=?"
    cursor.execute(query, str(project_id))
    conn.commit()
    conn.close()