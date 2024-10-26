import Run
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = Run.Runner('Alice')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Run.Runner('Andrew')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Run.Runner('Alice')
        runner2 = Run.Runner('Andrew')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

    class TournamentTest(unittest.TestCase):
        is_frozen = True

        @classmethod
        def setUpClass(cls):
            cls.all_results = {}

        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def setUp(self):
            vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
            self.runners = {n: Run.Runner(name=n, speed=v) for n, v in vs.items()}

        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def test_tournament1(self):
            tour = Run.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
            all_results = tour.start()
            self.assertTrue(all_results[2], self.runners['Ник'])

        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def test_tournament2(self):
            tour = Run.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
            all_results = tour.start()
            self.assertTrue(all_results[2], self.runners['Ник'])

        @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
        def test_tournament3(self):
            tour = Run.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
            all_results = tour.start()
            self.assertTrue(all_results[3], self.runners['Ник'])

        @classmethod
        def tearDownClass(cls):
            for k, v in cls.all_results.items():
                print(f'{k}: {v}')

    if __name__ == "__main__":
        unittest.main()