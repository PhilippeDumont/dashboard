import sqlite3


TABLES = {
    'items': (
    "CREATE TABLE  IF NOT EXISTS `items` ("
    "  `item_id` int NOT NULL,"
    "  `item_type` varchar(50) NOT NULL,"
    "  `value` varchar(50) NULL,"
    "  `parent_id` int NULL,"
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


def run():
    conn = sqlite3.connect('dashboard.db')
    _init_database(conn)
    return 'The DB was created'


def _init_database(conn):
    cursor = conn.cursor()
    print('Creating the db')
    _create_tables(cursor)
    cursor.close()


def _create_tables(cursor):
    print('Creating tables')
    for name in TABLES:
        query = TABLES[name]
        try:
            cursor.execute(query)
        except sqlite3.Error as err:
            print(err.args[0])
        print('Tables created')


def _reset_database():
    conn = sqlite3.connect('dashboard.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM activities')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="activities"')
    cursor.execute('DELETE FROM items')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="items"')
    cursor.close()
