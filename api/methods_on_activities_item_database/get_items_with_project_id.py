import sqlite3
from model.item_model import Item


def run(project_id):
    conn = sqlite3.connect("api/database_files/act_it_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    query = ("SELECT * FROM items")
    cursor.execute(query)
    list_items = list()
    for row in cursor:
        # Get all the Items linked to a project and put it into an Item object
        item_temp = Item(row[0], row[1], row[2], row[3], row[4])
        list_items.append(item_temp)
    cursor.close()
    return list_items
