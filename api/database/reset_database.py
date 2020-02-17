"""
Reset the database by deleting all the data
"""
def run(conn):
    cursor = conn.cursor()
    _reset_database(cursor)
    cursor.close()


def _reset_database(cursor):
    cursor.execute('DELETE FROM activities')
    cursor.execute('DELETE FROM items')