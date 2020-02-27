import sqlite3
import unittest
from datetime import date

from methods_on_project_database import update_project_last_opening_date
project_id = 1


class TestUpdateDatabaseProject(unittest.TestCase):

    # test if the last_opening_date of the project is updated
    def test_update_last_opening_date_project(self):
        update_project_last_opening_date.run(project_id)
        conn = sqlite3.connect('../database_files/project_db/all_project.db')
        cursor = conn.cursor()
        query = """SELECT last_opening_date from projects WHERE id = ?"""
        cursor.execute(query, str(project_id))
        self.assertEqual(cursor.fetchone()[0], date.today().isoformat())
