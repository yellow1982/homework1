import unittest

import module_12_1
import module_12_2

homeworkTS = unittest.TestSuite()
homeworkTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
homeworkTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(homeworkTS)