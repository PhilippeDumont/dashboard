import unittest
import sqlite3
from Database import init_database
from methods_on_csv import import_activity_csv
from methods_on_csv import import_item_csv

conn = sqlite3.connect('../dashboard.db')
linkCSV = "../Data_format"


class TestDB(unittest.TestCase):
    init_database.run_create(conn)
    import_activity_csv.run(conn, linkCSV + "/activity_data.csv")
    import_item_csv.run(conn, linkCSV + "/item_data.csv")
