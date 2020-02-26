import unittest
import sqlite3
from database import reset_database_activities_items
from database import reset_database_projects

unittest.TestLoader.sortTestMethodsUsing = None

project_id = 1


class TestResetDB(unittest.TestCase):

    # test of database activity and item reset
    def test_reset_database_activity_item(self):
        # reset database activities and items
        reset_database_activities_items.run(project_id)
        conn = sqlite3.connect("../database_files/act_it_db/" + str(project_id) + ".db")
        cursor = conn.cursor()
        cursor.execute('''SELECT count(*) FROM activities''')
        self.assertEqual(cursor.fetchone()[0], 0)
        cursor.execute('''SELECT count(*) FROM items''')
        self.assertEqual(cursor.fetchone()[0], 0)
        cursor.close()
        conn.commit()

    # test of database project reset
    def test_reset_database_project(self):
        conn = sqlite3.connect("../database_files/project_db/all_project.db")
        # reset database project as all_project.db
        reset_database_projects.run(conn)
        cursor = conn.cursor()
        cursor.execute('''SELECT count(*) FROM projects''')
        self.assertEqual(cursor.fetchone()[0], 0)
        cursor.close()
        conn.commit()
