import unittest
import sqlite3

from import_in_database import update_activity_item

unittest.TestLoader.sortTestMethodsUsing = None

linkCSV = "../data_format"
project_id = 1


class TestUpdateDB(unittest.TestCase):

    # test of database activity and item update
    def test_is_database_activities_updated(self):
        # update data from database
        update_activity_item.run(project_id, linkCSV + "/activity_data-test.csv", linkCSV + "/item_data-test.csv")
        # connect to database
        conn = sqlite3.connect("../databases_files/activities_items_db/" + str(project_id) + ".db")
        # create the cursor
        cursor = conn.cursor()
        # get the count of activities
        cursor.execute('''SELECT count(*) FROM activities''')
        self.assertEqual(cursor.fetchone()[0], 3)
        # get the count of items
        cursor.execute('''SELECT count(*) FROM items''')
        self.assertEqual(cursor.fetchone()[0], 2)
        cursor.close()
        conn.commit()
