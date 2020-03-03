from methods_on_activities_items_database import get_activities_with_project_id, get_items_with_project_id
from methods_on_project_database import get_project_with_id
from model.activities_items_project_model import ActivitiesItemsProject


def run(project_id):
    list_activities = get_activities_with_project_id.run(project_id)
    list_item = get_items_with_project_id.run(project_id)
    project = get_project_with_id.run(project_id)
    activities_items_project = ActivitiesItemsProject(list_activities, list_item, project)
    return activities_items_project
