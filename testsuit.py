import unittest


testsuite = unittest.TestSuite()

loader = unittest.TestLoader().discover(start_dir='test',pattern='case*.py')
testsuite.addTests(loader)


runner = unittest.TextTestRunner()
runner.run(testsuite)