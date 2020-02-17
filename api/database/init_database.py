import sqlite3
import logging
from database import reset_database
import sys

TABLES = {
    'items': (
    "CREATE TABLE  IF NOT EXISTS `items` ("
    "  `item_id` varchar(200) NOT NULL,"
    "  `item_type` varchar(50) NOT NULL,"
    "  `value` varchar(1000) NULL,"
    "  `parent_id` varchar(200) NULL,"
    "  `parent_type` varchar(50) NULL,"
    "  PRIMARY KEY (`item_id`, `item_type`),"
    "  CONSTRAINT `fk_items_items` FOREIGN KEY (`parent_id`, `parent_type`)"
    "     REFERENCES `items` (`item_id`, `item_type`) ON DELETE NO ACTION ON UPDATE NO ACTION"
    ");"),
    'activities': (
    "CREATE TABLE  IF NOT EXISTS `activities` ("
    "  `activity_id` int NOT NULL,"
    "  `context_id` int NULL,"
    "  `context_type` varchar(50) NULL,"
    "  `object_id` int NULL,"
    "  `object_type` varchar(50) NULL,"
    "  `subject_id` int NULL,"
    "  `subject_type` varchar(50) NULL,"
    "  `date` datetime NOT NULL,"
    "  `activity_type` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`activity_id`),"
    "  CONSTRAINT `fk_activities_items_1` FOREIGN KEY (`context_id`, `context_type`)"
    "     REFERENCES `items` (`item_id`, `item_type`) ON DELETE NO ACTION ON UPDATE NO ACTION,"
    "  CONSTRAINT `fk_activities_items_2` FOREIGN KEY (`subject_id`, `subject_type`)"
    "     REFERENCES `items` (`item_id`, `item_type`) ON DELETE NO ACTION ON UPDATE NO ACTION,"
    "  CONSTRAINT `fk_activities_items_3` FOREIGN KEY (`object_id`, `object_type`)"
    "     REFERENCES `items` (`item_id`, `item_type`) ON DELETE NO ACTION ON UPDATE NO ACTION"
    ");")
    }


def run(conn):
    _init_database(conn)
    print('The DB was created')
    sys.stdout.flush()


def _init_database(conn):
    cursor = conn.cursor()
    logging.info('Init database')
    _create_tables(cursor)
    cursor.close()


def _create_tables(cursor):
    for name in TABLES:
        query = TABLES[name]
        try:
            logging.info("Creating table %s", name)
            cursor.execute(query)
        except sqlite3.Error as err:
            logging.error('Error: %s', err.args[0])
        logging.info("Table %s successfully created", name)

def _test_if_exist(conn):
    cursor = conn.cursor()
    # get the count of tables with the name
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='activities' ''')
    # if the count is 1, then table exists
    if cursor.fetchone()[0] == 1:
        reset_database.run(conn)
    # commit the changes to db
    conn.commit()




conn = sqlite3.connect('example.db')
print('The DB was created')
run(conn)
sys.stdout.flush()
