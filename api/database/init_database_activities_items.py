import sqlite3
import logging
import os
from methods_on_project_database import get_project_id_with_name

# Is the String that makes the tables
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


def run(project_name):
    try:
        # Create the path to the database
        if not os.path.exists("../database_files/act_it_db"):
            os.makedirs("../database_files/act_it_db")
    except Exception as err:
        logging.error(err)
    # Get the id by the name of the project
    project_id = get_project_id_with_name.run(project_name)
    conn = sqlite3.connect("../database_files/act_it_db/" + str(project_id) + ".db")
    # Create the database with the connection
    _init_database(conn)
    conn.commit()
    # Return the project id to the front end
    return project_id


def _init_database(conn):
    cursor = conn.cursor()
    logging.info('Init database')
    _create_tables(cursor)
    cursor.close()


# Create the database with the tables information
def _create_tables(cursor):
    for name in TABLES:
        query = TABLES[name]
        try:
            logging.info("Creating table %s", name)
            cursor.execute(query)
        except sqlite3.Error as err:
            logging.error('Error: %s', err.args[0])
        logging.info("Table %s successfully created", name)
