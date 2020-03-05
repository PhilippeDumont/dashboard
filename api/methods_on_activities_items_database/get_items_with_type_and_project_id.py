import sqlite3
from model.item_model import Item

# Methods to get items for a project (with project_id) and of a certain type
def run(project_id, item_type):
    conn = sqlite3.connect("../databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    # Get items of a certain type
    query = """SELECT * FROM items WHERE item_type = ?"""
    cursor.execute(query, item_type)
    # Create a list of items we get from the transaction with the database
    list_items = list()
    try:
        for row in cursor:
            temp = Item(row[0], row[1], row[2], row[3], row[4])
            list_items.append(temp)
    except Exception as e:
        cursor.close()
        msgError = "No items with this kind of type in the project"
        return msgError
    cursor.close()
    return list_items
