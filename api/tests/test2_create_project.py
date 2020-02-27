import unittest
import sqlite3
from import_in_database import create_project

project_name = "project1"


class TestCreateProject(unittest.TestCase):

    def test_create_project(self):
        # database project is filled
        # database activities and items created
        response = create_project.run(project_name)
        self.assertEqual(response, 1)
        # connect to database
        conn = sqlite3.connect("../database_files/act_it_db/1.db")
        # create the cursor
        cursor = conn.cursor()
        # get the count of tables with the name
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='activities' ''')
        # if the count is 1, then table exists
        self.assertEqual(cursor.fetchone()[0], 1)
        # close the cursor
        cursor.close()  # OK

        conn.commit()
