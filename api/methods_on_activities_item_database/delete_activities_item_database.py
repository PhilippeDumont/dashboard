import os
import sqlite3


def run(project_id):
    os.remove("api/database_files/act_it_db/" + str(project_id) + ".db")