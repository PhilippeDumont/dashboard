import unittest
from Database import init_database


class TestDB(unittest.TestCase):
    init_database.run()
