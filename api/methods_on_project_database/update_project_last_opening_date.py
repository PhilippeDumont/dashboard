"""
Update the "last_opening_date" of the project
"""
import sqlite3
from datetime import datetime


def run(project_id):
    conn = sqlite3.connect('api/databases_files/projects_db/all_project.db')
    cursor = conn.cursor()
    date_today = datetime.now()
    query = """UPDATE projects SET last_opening_date = ? WHERE id = ?"""
    data = (date_today, str(project_id))
    cursor.execute(query, data)
    conn.commit()
