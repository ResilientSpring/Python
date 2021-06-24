import unittest
import datetime
import genetic
import random


def create(numbers, operations, minNumbers, maxNumbers):
    genes = [random.choice(numbers)]
    count = random.randint(a=minNumbers, b=1 + maxNumbers)
    while count > 1:
        count -= 1
        genes.append(random.choice(operations))
        genes.append(random.choice(numbers))

    return genes

class EquationGenerationTests(unittest.TestCase):
    def test(self):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        operations = ['+', '-']