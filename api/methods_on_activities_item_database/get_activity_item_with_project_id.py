from methods_on_activities_item_database import get_activities_with_project_id, get_items_with_project_id
from model.activities_items_model import ActivitiesItems


def run(project_id):
    list_activities = get_activities_with_project_id.run(project_id)
    list_item = get_items_with_project_id.run(project_id)
    list_to_return = ActivitiesItems(list_activities, list_item, project_id)
    return list_to_return
