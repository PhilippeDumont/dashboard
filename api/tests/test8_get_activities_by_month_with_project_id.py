import unittest

from methods_on_activities_items_database import get_activities_by_month_with_project_id


class TestGetActivitiesByMonthWithProjectId(unittest.TestCase):

    def test_get_activities_by_month_with_project_id(self):
        # get an array of activities from the minimum month to the latest month
        array_result = get_activities_by_month_with_project_id.run(1)
        self.assertEqual(array_result[0], 1)
        for cpt in range(1, 13):
            self.assertEqual(array_result[cpt], 0)
        self.assertEqual(array_result[13], 1)
        print(str(array_result) + str(len(array_result)))


if __name__ == '__main__':
    unittest.main()
