import unittest

# method to run all tests in the right order
if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1).run(test_suite)
