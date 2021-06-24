import unittest
import datetime
import genetic
import random


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(
        (' '.join(map(str, [i for i in candidate.Genes]))),
        candidate.Fitness,
        timeDiff))


def create(numbers, operations, minNumbers, maxNumbers):
    genes = [random.choice(numbers)]
    count = random.randint(a=minNumbers, b=1 + maxNumbers)
    while count > 1:
        count -= 1
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))

    return genes


def mutate(genes, numbers, operations, minNumbers, maxNumbers):
    numberCount = (1 + len(genes)) / 2
    adding = numberCount < maxNumbers and random.randint(a=0, b=100) == 0

    if adding:
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))

        return

    removing = numberCount > minNumbers and random.randint(a=0, b=20) == 0

    if removing:
        index = random.randrange(start=0, step=len(genes) - 1)
        del genes[index]
        del genes[index]
        return

    index = random.randrange(0, len(genes))
    genes[index] = random.choice(operations) if (index & 1) == 1 else random.choice(numbers)


class EquationGenerationTests(unittest.TestCase):
    def test(self):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        operations = ['+', '-']
