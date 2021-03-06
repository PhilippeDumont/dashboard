# -*- coding: utf-8 -*-
import os
import unittest
import sqlite3
from database import init_database_project


class TestInitDB(unittest.TestCase):

    def test_init_database_project(self):
        # test if database exist
        exist = os.path.exists("../databases_files/activities_items_db/all_project.db")
        self.assertFalse(exist)
        # init the database to the connected file
        init_database_project.run()
        # connect to database
        conn = sqlite3.connect("../databases_files/projects_db/all_project.db")
        # create the cursor
        cursor = conn.cursor()
        # get the count of tables with the name
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='projects' ''')
        # if the count is 1, then table exists
        self.assertEqual(cursor.fetchone()[0], 1)
        # close the cursor
        cursor.close()

        conn.commit()
