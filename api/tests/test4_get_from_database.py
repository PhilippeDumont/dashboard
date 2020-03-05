# -*- coding: utf-8 -*-
import unittest
from methods_on_project_database import get_projects, get_project_with_id, project_not_exist
from methods_on_project_database import get_project_id_with_name
from methods_on_activities_items_database import get_activities_with_project_id, \
    get_activities_items_project_with_project_id, get_items_with_project_id, get_activities_items_with_project_id

unittest.TestLoader.sortTestMethodsUsing = None

project_id_to_search = 1
project_name = "project1"


class TestGetFromDB(unittest.TestCase):

    # test query all projects
    def test_get_projects_from_db(self):
        list_project = get_projects.run()
        self.assertEqual(list_project[0].get("id"), 1)

    # test query one project
    def test_get_project_from_db(self):
        project_id = get_project_id_with_name.run("project1")
        self.assertEqual(project_id, 1)

    # test query project by project_id
    def test_get_project_with_id(self):
        project_id = get_project_with_id.run(project_id_to_search)
        self.assertEqual(project_id.get("id"), 1)

    # test if project exists
    def test_if_project_exist(self):
        chose_project = project_not_exist.run(project_name)
        self.assertEqual(chose_project, False)

    # test query activities by project_id
    def test_get_activities_with_project_id(self):
        list_activities = get_activities_with_project_id.run(project_id_to_search)
        self.assertEqual(len(list_activities), 1)

    # test query items by project_id
    def test_get_items_with_project_id(self):
        list_items = get_items_with_project_id.run(project_id_to_search)
        self.assertEqual(len(list_items), 1)

    # test query activities, items and project by project_id
    def test_get_activity_item_project_with_project_id(self):
        object_temp = get_activities_items_project_with_project_id.run(project_id_to_search)
        self.assertEqual(len(object_temp.activities), 1)
        self.assertEqual(len(object_temp.items), 1)
        self.assertEqual(object_temp.project.get("id"), 1)

    # test query activities, items and project
    def test_get_activity_item_with_project_id(self):
        object_temp = get_activities_items_with_project_id.run(project_id_to_search)
        self.assertEqual(len(object_temp.activities), 1)
        self.assertEqual(len(object_temp.items), 1)
        self.assertEqual(object_temp.project_id, 1)