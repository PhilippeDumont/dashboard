import sqlite3


def run(project_id, project_new_name):
    conn = sqlite3.connect("api/databases_files/projects_db/all_project.db")
    cursor = conn.cursor()
    query = """UPDATE projects SET name = ? WHERE id = ?"""
    data = (project_new_name, str(project_id))
    cursor.execute(query,data)
    conn.commit()