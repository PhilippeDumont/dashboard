import unittest
import sqlite3

from methods_on_activities_item_database import delete_activities_item_database

project_id = 1


class TestDeleteproject(unittest.TestCase):

    # test of delete a project
    def delete_project(self):
        delete_activities_item_database.run(project_id)
        conn = sqlite3.connect("../database_files/project_db/all_project.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM projects WHERE id = ?''', project_id)
        self.assertEqual(cursor.fetchone(), 0)
        cursor.close()
        conn.commit()
