import sqlite3
from model.activity_model import Activity


def run(project_id, type_necessary, date_start, date_end):
    conn = sqlite3.connect("api/databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    query = """SELECT * FROM activities WHERE activity_type = ? AND date BETWEEN date(?) AND date(?)"""
    dataset = (type_necessary, date_start, date_end)
    cursor.execute(query, dataset)
    list_activities = list()
    try:
        for row in cursor:
            # Get all activities linked to the database and put it into an activity object
            project_temp = Activity(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            list_activities.append(project_temp)
    except Exception as err:
        cursor.close()
        message = "No activities in this interval of dates or with this type in this project"
        return message
    cursor.close()
    return list_activities
