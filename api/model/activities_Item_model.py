from model.activity_model import Activity


class ActivitiesItem:
    activities: list
    items: list
    project_id: int

    def __init__(self, activities, items, project_id):
        self.activities = activities
        self.items = items
        self.project_id = project_id
