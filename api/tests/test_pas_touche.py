import unittest

from methods_on_activities_items_database.get_activities_for_hours_in_week_by_day_by_project_id import \
    get_activities_for_hours_in_week_by_day_by_project_id


class TestPasTouche(unittest.TestCase):

    def test_pas_touche(self):
        get_activities_for_hours_in_week_by_day_by_project_id(1, "1990-10-08", "1990-11-08")


if __name__ == '__main__':
    unittest.main()
