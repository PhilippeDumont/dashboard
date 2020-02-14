from datetime import datetime
import logging
import sqlite3


def save_activity_in_db(cursor, activity):
    """
    Save one activity in the db
    """
    activity_id = activity['activity_id']

    date = datetime.fromisoformat(activity['date'])

    subject_id = activity['subject_id']
    subject_type = activity['subject_type']

    activity_type = activity['activity_type']

    object_id = activity['object_id']
    object_type = activity['object_type']

    context_id = activity.get('context_id')
    context_type = activity.get('context_type')

    query_log = '''INSERT INTO activities 
                        (activity_id, date, subject_id, subject_type, activity_type, object_id, object_type, context_id, context_type)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    data_log = (activity_id, date, subject_id, subject_type, activity_type, object_id, object_type, context_id, context_type)
    try:
        cursor.execute(query_log, data_log)
    except sqlite3.Error as e:
        logging.error(e.args[0])


def save_item_in_db(cursor, item):
    """
    Save one item in db
    """
    item_id = item["item_id"]
    item_type = item["item_type"]
    value = item.get("value")

    parent_id = item.get("parent_id")
    parent_type = item.get("parent_type")

    query_item = '''INSERT INTO items (item_id, item_type, value, parent_id, parent_type) 
                        VALUES (?,?,?,?,?)'''
    data_item = (item_id, item_type, value, parent_id, parent_type)

    try:
        cursor.execute(query_item, data_item)
    except sqlite3.Error as e:
        logging.error(e.args[0])

