import sqlite3
from model.activity_model import Activity


def run(project_id):
    conn = sqlite3.connect("api/databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    query = ("SELECT * FROM activities")
    cursor.execute(query)
    list_activities = list()
    for row in cursor:
        # Get all activities linked to the database and put it into an activity object
        project_temp = Activity(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        list_activities.append(project_temp)
    cursor.close()
    return list_activities
