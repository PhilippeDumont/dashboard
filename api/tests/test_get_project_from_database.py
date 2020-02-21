# -*- coding: utf-8 -*-
import unittest
from model.project_model import Project
from methods_on_project_database import get_projects, get_project_with_id, project_exist
from methods_on_project_database import get_project_id_with_name

unittest.TestLoader.sortTestMethodsUsing = None

project_id_to_search = 1
project_name = "test_project"


class TestGetFromDB(unittest.TestCase):

    def test_get_projects_from_db(self):
        list_project = get_projects.run()
        self.assertEqual(list_project[0].id, 1)

    def test_get_project_from_db(self):
        project_id = get_project_id_with_name.run("ProjectTestSubject")
        self.assertEqual(project_id, 1)

    def test_get_project_with_id(self):
        project_id = get_project_with_id.run(project_id_to_search)
        self.assertEqual(project_id, 1)

    def test_if_project_exist(self):
        chose_project = project_exist.run(project_name)
        self.assertEqual(chose_project, project_name)