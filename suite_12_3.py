import unittest
import tests_12_2
import tests_12_3

try_1 = unittest.TestSuite()
try_1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
try_1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(try_1)