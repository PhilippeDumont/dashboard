# -*- coding: utf-8 -*-
import unittest
from model.project_model import Project
from methods_on_database import get_projects
from methods_on_database import get_project_id_with_name
unittest.TestLoader.sortTestMethodsUsing = None


class TestGetFromDB(unittest.TestCase):

    def test_get_projects_from_db(self):
        list_project = get_projects.run()
        self.assertEqual(list_project[0].id, 1)

    def test_get_project_from_db(self):
        project_id = get_project_id_with_name.run("ProjectTestSubject")
        self.assertEqual(project_id, 1)
