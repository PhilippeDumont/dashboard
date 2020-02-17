# -*- coding: utf-8 -*-
import unittest
import sqlite3
from database import init_database_activities_items
from database import init_database_project
unittest.TestLoader.sortTestMethodsUsing = None

db_act_it_name = "project1.db"
# LAUNCH THIS TEST BEFORE ANYTHING ELSE !!!


class TestInitDB(unittest.TestCase):

    def test_is_database_project(self):
        # init the database to the connected file
        init_database_project.run()
        # connect to database
        conn = sqlite3.connect("../database_files/project_db/all_project.db")
        # create the cursor
        cursor = conn.cursor()
        # get the count of tables with the name
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='projects' ''')
        # if the count is 1, then table exists
        self.assertEqual(cursor.fetchone()[0], 1)
        # close the cursor
        cursor.close()

        conn.commit()

    def test_is_database_activities_items_created(self):
        # init the database to the connected file
        init_database_activities_items.run(db_act_it_name)
        # connect to database
        conn = sqlite3.connect("../database_files/act_it_db/project1.db")
        # create the cursor
        cursor = conn.cursor()
        # get the count of tables with the name
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='activities' ''')
        # if the count is 1, then table exists
        self.assertEqual(cursor.fetchone()[0],1)
        # close the cursor
        cursor.close()         # OK

        conn.commit()
