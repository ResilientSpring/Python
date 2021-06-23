import unittest
import datetime
import genetic

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        timeDiff))


def get_fitness(genes):
    fitness = 1

    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
            return fitness


class SortedNumbersTest(unittest.TestCase):

    def test_sort_10_numbers(self):
        self.sort_numbers(10)

    def sort_numbers(self, totalNumbers):
        geneset = [i for i in range(100)]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate=candidate, startTime=startTime)

        def fnGetFitness(genes):
            return get_fitness(genes)


        optimalFitness = totalNumbers
        best = genetic.get_best(get_fitness=fnGetFitness, targetLen=totalNumbers,
                                optimalFitness=optimalFitness, geneSet=geneset, display=fnDisplay)

        self.assertTrue(not optimalFitness > best.Fitness)


    def get_fitness(self, genes):
        fitness = 1
        for i in range(len(genes)):
            if genes[i] > genes[i - 1]:
                fitness += 1

        return fitness