import os
import unittest
import sqlite3
from methods_on_project_database import delete_project

project_id = 1


class TestDeleteProject(unittest.TestCase):

    # test of delete a project
    def test_delete_project(self):
        # delete database file for activities and items
        delete_project.run(project_id)
        conn = sqlite3.connect("../database_files/project_db/all_project.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT count(*) FROM projects WHERE id = ?''', str(project_id))
        self.assertEqual(cursor.fetchone()[0], 0)
        cursor.close()
        conn.commit()
        exist = os.path.exists("../database_files/act_it_db/" + str(project_id) + ".db")
        self.assertFalse(exist)
