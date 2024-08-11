import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(key)
            for key2, value2 in value.items():
                print(key2, value2)
            print('_________\n')

    def test_tournament1(self):
        tournament = Tournament(90, self.r1, self.r3)
        result = tournament.start()
        self.all_results['Тест 1'] = result
        self.assertTrue(result[2] == self.r3)

    def test_tournament2(self):
        tournament = Tournament(90, self.r2, self.r3)
        result = tournament.start()
        self.all_results['Тест 2'] = result
        self.assertTrue(result[2] == self.r3)

    def test_tournament3(self):
        tournament = Tournament(90, self.r1, self.r2, self.r3)
        result = tournament.start()
        self.all_results['Тест 3'] = result
        self.assertTrue(result[3] == self.r3)


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
