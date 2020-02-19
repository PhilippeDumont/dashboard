import logging
import sqlite3
import unittest
from import_in_database import create_project
project_name = "ProjectTestSubject"


class TestFillProjectDatabase(unittest.TestCase):

    def test_create_project(self):
        create_project.run(project_name)
        conn = sqlite3.connect("../database_files/project_db/all_project.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        self.assertEqual(cursor.fetchone()[0], 1)
        cursor.close()
        conn.close()
