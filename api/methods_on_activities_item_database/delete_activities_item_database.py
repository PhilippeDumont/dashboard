import os


def run(project_id):
    os.remove("api/databases_files/activities_items_db/" + str(project_id) + ".db")
