from model.project_model import Project


class ActivitiesItemsProject:
    activities: list
    items: list
    project: Project

    def __init__(self, activities, items, project):
        self.activities = activities
        self.items = items
        self.project = project
