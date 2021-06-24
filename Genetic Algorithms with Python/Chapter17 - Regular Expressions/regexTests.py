import datetime
import unittest

repeatMetas = {'?', '*', '+'}
startMetas = {'|'}
allMetas = repeatMetas | startMetas

class RegexTests(unittest.TestCase):
    def test_two_digits(self):
        wanted = {'01', '01', '11', '10'}
        unwanted = ['00', '']

        self.find_regex(wanted, unwanted, 7)


    def find_regex(self, wanted, unwanted, expectedLength, customOperators=None):
        startTime = datetime.datetime.now()
        textGenes = wanted | set(c for w in wanted for c in w)
        fullGeneset = [i for i in allMetas | textGenes]