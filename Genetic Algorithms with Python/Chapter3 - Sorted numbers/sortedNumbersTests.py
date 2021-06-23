import unittest

def get_fitness(genes):
    fitness = 1
    gap = 0

    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)


class SortedNumbersTests(unittest.TestCase):
    def test_sort_10_numbers(self):
        self.sort_numbers(10)

    def sort_numbers(self, totalNumbers):
        geneset = [i for i in range(100)]


class Fitness:
    def __init__(self, numbersInSequenceCount, totalGap):
        self.NumbersInSequenceCount = numbersInSequenceCount
        self.TotalGap = totalGap

    def __gt__(self, other):
        if self.NumbersInSequenceCount != other.NumbersInSequenceCount:
            return self.NumbersInSequenceCount > other.NumbersInSequenceCount
        return self.TotalGap < other.TotalGap

    def __str__(self):
        return "{} Sequential, {} Total Gap".format(
            self.NumbersInSequenceCount,
            self.TotalGap)

