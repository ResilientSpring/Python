import unittest
import datetime


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        timeDiff))


class SortedNumbersTest(unittest.TestCase):

    def test_sort_10_numbers(self):
        self.sort_numbers(10)

    def sort_numbers(self, totalNumbers):
        geneset = [i for i in range(100)]

    def get_fitness(self, genes):
        fitness = 1
        for i in range(len(genes)):
            if genes[i] > genes[i - 1]:
                fitness += 1

        return fitness

