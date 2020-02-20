from methods_on_act_it_database import get_activities_with_project_id, get_items_with_project_id
from model.activities_Item_model import ActivitiesItem


def run(project_id):
    list_activities = get_activities_with_project_id.run(project_id)
    list_item = get_items_with_project_id.run(project_id)
    list_to_return = ActivitiesItem(list_activities, list_item, project_id)
    return list_to_return
