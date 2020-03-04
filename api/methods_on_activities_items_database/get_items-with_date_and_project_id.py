import sqlite3
from model.item_model import Item

# Methods to get items for a project (with project_id) and in a time interval
def run(project_id, begin_date, end_date):
    conn = sqlite3.connect("api/databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    # Get items in a time interval => INNER JOIN because the row date is in the table activities
    query = """SELECT * FROM items INNER JOIN activities ON items.parent_id = activities.activity_id WHERE activities.date BETWEEN date(?) AND date(?)"""
    dataset = (begin_date, end_date)
    cursor.execute(query, dataset)
    # Create a list of items we get from the transaction with the database
    list_items = list()
    try:
        for row in cursor:
            temp = Item(row[0], row[1], row[2], row[3], row[4])
            list_items.append(temp)
    except Exception as e:
        cursor.close()
        msgError = "No items in this time interval in the project"
        return msgError
    cursor.close()
    return list_items