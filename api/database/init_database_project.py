import sqlite3
import logging
import os

TABLES = {
    'projects': (
    "CREATE TABLE IF NOT EXISTS `projects` ("
    "  `id` INTEGER PRIMARY KEY AUTOINCREMENT,"
    "  `name` varchar(200) NOT NULL,"
    "  `creation_date` datetime NOT NULL,"
    "  `last_opening_date` datetime NOT NULL,"
    "  `nb_activities` INTEGER NOT NULL,"
    "  `nb_items` INTEGER NOT NULL"
    ");")
    }


def run():
    try:
        if not os.path.exists("../database_files/project_db"):
            os.makedirs("../database_files/project_db")
    except Exception as err:
        logging.error(err)
    conn = sqlite3.connect("../database_files/project_db/all_project.db")
    _init_database(conn)
    conn.commit()
    return 'The DB was created'


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


"""def _test_if_exist(conn):
    cursor = conn.cursor()
    # get the count of tables with the name
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='projects' ''')
    # if the count is 1, then table exists
    if cursor.fetchone()[0] == 1:
        reset_database_activities_items.run(conn)
    # commit the changes to db
    conn.commit()"""