import unittest
import sqlite3
from methods_on_project_database import rename_project

class RenameProject(unittest.TestCase):

    def test_rename_project(self):
        rename_project.run(1, "leMeilleurProjet")
        conn = sqlite3.connect("../databases_files/projects_db/all_project.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM projects WHERE id = ? """)
        self.assertEqual("leMeilleurProjet", cursor.fetchone()[0])

if __name__ == '__main__':
    unittest.main()
