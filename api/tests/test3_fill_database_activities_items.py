from methods_on_csv import import_activity_csv
from methods_on_csv import import_item_csv
import unittest
import sqlite3

unittest.TestLoader.sortTestMethodsUsing = None

linkCSV = "../csv_test"


class TestFillDBActivitiesAndItem(unittest.TestCase):

    def test_is_activity_imported(self):
        # import one line of data in the database
        import_activity_csv.run("1", linkCSV + "/activity_data.csv")
        conn = sqlite3.connect("../databases_files/activities_items_db/1.db")
        cursor = conn.cursor()
        # get the data back from the database
        cursor.execute('''SELECT * FROM activities''')
        # test if we get the good value
        self.assertEqual(cursor.fetchone()[0], 1)
        cursor.close()

    def test_is_item_imported(self):
        # import one line of data in the database
        import_item_csv.run("1", linkCSV + "/item_data.csv")
        conn = sqlite3.connect("../databases_files/activities_items_db/1.db")
        cursor = conn.cursor()
        # get the data back from the database
        cursor.execute('''SELECT * FROM items''')
        # test if we get the good value
        self.assertEqual(cursor.fetchone()[0], "553ff7e745b3c39afa00012c")
        cursor.close()
