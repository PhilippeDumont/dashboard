# -*- coding: utf-8 -*-
import unittest
from model.project_model import Project
from methods_on_database import get_projects
unittest.TestLoader.sortTestMethodsUsing = None

db_act_it_name = "project1"
# LAUNCH THIS TEST BEFORE ANYTHING ELSE !!!


class TestGetFromDB(unittest.TestCase):

    def test_get_project_from_db(self):
        list_project = get_projects.run()
        self.assertEqual(list_project[0].id, 1)