import datetime
import sqlite3
import unittest
from datetime import datetime
import logging

from methods_on_project_database import update_project_last_opening_date
project_id = 1


class TestUpdateDatabaseProject(unittest.TestCase):
    def test_update_last_opening_date_project(self):
        update_project_last_opening_date.run(project_id)
        conn = sqlite3.connect('../database_files/project_db/all_project.db')
        cursor = conn.cursor()
        query = """SELECT last_opening_date from projects WHERE id = ?"""
        cursor.execute(query, str(project_id))
        date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_str = cursor.fetchone()[0].split(".")
        self.assertEqual(date_str[0], date_today)