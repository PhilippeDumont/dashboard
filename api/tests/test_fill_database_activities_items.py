from methods_on_csv import import_activity_csv
from methods_on_csv import import_item_csv
import unittest
import sqlite3
unittest.TestLoader.sortTestMethodsUsing = None

conn_in_project = sqlite3.connect('../dashboard_project.db')
conn_in_activities_items = sqlite3.connect('../dashboard_activities_items.db')
linkCSV = "../data_format"


class TestFillDBActivitiesAndItem(unittest.TestCase):

    def test_is_activity_imported(self):
        # import one line of data in the database
        import_activity_csv.run(conn_in_activities_items, linkCSV + "/activity_data.csv")
        cursor = conn_in_activities_items.cursor()
        # get the data back from the database
        cursor.execute('''SELECT * FROM activities''')
        # test if we get the good value
        self.assertEqual(cursor.fetchone()[0], 1)
        cursor.close()

    def test_is_item_imported(self):
        # import one line of data in the database
        import_item_csv.run(conn_in_activities_items, linkCSV + "/item_data.csv")
        cursor = conn_in_activities_items.cursor()
        # get the data back from the database
        cursor.execute('''SELECT * FROM items''')
        # test if we get the good value
        self.assertEqual(cursor.fetchone()[0], "553ff7e745b3c39afa00012c")
        cursor.close()
