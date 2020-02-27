import sqlite3
from database import reset_database_activities_items
from methods_on_csv import import_item_csv
from methods_on_csv import import_activity_csv


def run(project_id, path_act, path_item):
    conn = sqlite3.connect("api/database_files/act_it_db/" + str(project_id) + ".db")
    reset_database_activities_items.run(project_id)
    conn.commit()
    conn.close()
    _reimportation_of_data(project_id, path_act, path_item)


def _reimportation_of_data(project_id, path_act, path_item):
    import_activity_csv.run(project_id, path_act)
    import_item_csv.run(project_id, path_item)
