# -*- coding: utf-8 -*-
import unittest
import sqlite3
import logging
from database import init_database
from methods_on_csv import import_activity_csv
from methods_on_csv import import_item_csv

conn = sqlite3.connect('../dashboard.db')
linkCSV = "../Data_format"


class TestDB(unittest.TestCase):
    init_database.run(conn)

    def test_is_database_created(self):
        cursor = conn.cursor()
        # get the count of tables with the name
        cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='activities' ''')
        # if the count is 1, then table exists
        self.assertEqual(cursor.fetchone()[0],1)
        # close the cursor
        cursor.close()                                                       # OK

    def test_is_item_imported(self):
        # import one line of data in the database
        import_item_csv.run(conn, linkCSV + "/item_data.csv")
        cursor = conn.cursor()
        # get the data back from the database
        cursor.execute('''SELECT * FROM items''')
        # test if we get the good value
        self.assertEqual(cursor.fetchone()[0], "553ff7e745b3c39afa00012c")
        cursor.close()


    def test_is_activity_imported(self):
        # import one line of data in the database
        import_activity_csv.run(conn, linkCSV + "/activity_data.csv")
        cursor = conn.cursor()
        # get the data back from the database
        cursor.execute('''SELECT * FROM activities''')
        # test if we get the good value
        self.assertEqual(cursor.fetchone()[0],1)
        cursor.close()
