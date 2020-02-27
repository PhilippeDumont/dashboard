import sqlite3
from datetime import date


def run(project_id):
    conn = sqlite3.connect('api/database_files/project_db/all_project.db')
    cursor = conn.cursor()
    date_today = date.today().isoformat()
    query = """UPDATE projects SET last_opening_date = ? WHERE id = ?"""
    data = (date_today, str(project_id))
    cursor.execute(query, data)
    conn.commit()
