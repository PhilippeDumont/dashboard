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
        conn = sqlite3.connect("../database_files/act_it_db/" + str(project_id) + ".db")
        cursor = conn.cursor()
        cursor.execute('''SELECT count(*) FROM activities''')
        self.assertEqual(cursor.fetchone()[0], 3)
        cursor.execute('''SELECT count(*) FROM items''')
        self.assertEqual(cursor.fetchone()[0], 2)
        cursor.close()
        conn.commit()
