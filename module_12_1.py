import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Runner")
        i = 0
        while i < 10:
            runner.walk()
            i += 1
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Runner")
        i = 0
        while i < 10:
            runner.run()
            i += 1
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Ranner1")
        runner2 = Runner("Ranner2")
        i = 0
        while i < 10:
            runner1.run()
            runner2.walk()
            i += 1
        self.assertNotEqual(runner1.distance, runner2.distance)


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


