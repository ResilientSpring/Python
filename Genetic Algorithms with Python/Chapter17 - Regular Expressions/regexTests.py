import datetime
import unittest
import re
import random
from functools import partial

repeatMetas = {'?', '*', '+', '{2}', '{2,}'}
startMetas = {'|', '(', '['}
endMetas = {')', ']'}
allMetas = repeatMetas | startMetas | endMetas

regexErrorsSeen = {}


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
        repair_regex(candidate.Genes), candidate.Fitness, timeDiff))


def repair_regex(genes):
    result = []
    finals = []
    f = repair_ignore_repeat_metas
    for token in genes:
        f = f(token, result, finals)
    if ']' in finals and result[-1] == '[':
        del result[-1]
    result.extend(reversed(finals))
    return ''.join(result)


def repair_ignore_repeat_metas(token, result, finals):
    if token in repeatMetas or token in endMetas:
        return repair_ignore_repeat_metas
    if token == '(':
        finals.append(')')
    result.append(token)
    if token == '[':
        finals.append(']')
        return repair_in_character_set
    return repair_ignore_repeat_metas_following_repeat_or_start_metas


def repair_ignore_repeat_metas_following_repeat_or_start_metas(token,
                                                               result,
                                                               finals):
    last = result[-1]
    if token not in repeatMetas:
        if token == '[':
            result.append(token)
            finals.append(']')
            return repair_in_character_set
        if token == '(':
            finals.append(')')
        elif token == ')':
            match = ''.join(finals).rfind(')')
            if match != -1:
                del finals[match]
            else:
                result[0:0] = ['(']
        result.append(token)
    elif last in startMetas:
        pass
    elif token == '?' and last == '?' and len(result) > 2 and \
            result[-2] in repeatMetas:
        pass
    elif last in repeatMetas:
        pass
    else:
        result.append(token)
    return repair_ignore_repeat_metas_following_repeat_or_start_metas


def repair_in_character_set(token, result, finals):
    if token == ']':
        if result[-1] == '[':
            del result[-1]
        result.append(token)
        match = ''.join(finals).rfind(']')
        if match != -1:
            del finals[match]
        return repair_ignore_repeat_metas_following_repeat_or_start_metas
    elif token == '[':
        pass
    elif token == '|' and result[-1] == '|':
        pass  # suppresses FutureWarning about ||
    else:
        result.append(token)
    return repair_in_character_set


def get_fitness(genes, wanted, unwanted):
    pattern = repair_regex(genes)
    length = len(pattern)

    try:
        re.compile(pattern)
    except re.error as e:
        key = str(e)
        key = key[:key.index("at position")]
        info = [str(e),
                "genes = ['{}']".format("', '".join(genes)),
                "regex: " + pattern]

        if key not in regexErrorsSeen or len(info[1]) < len(regexErrorsSeen[key][1]):
            regexErrorsSeen[key] = info

        return Fitness(0, len(wanted), len(unwanted), length)

    numWantedMatched = sum(1 for i in wanted if re.fullmatch(pattern, i))
    numUnwantedMatched = sum(1 for i in unwanted if re.fullmatch(pattern, i))

    return Fitness(numWantedMatched, len(wanted), numUnwantedMatched,
                   length)


def mutate(genes, fnGetFitness, mutationOperators, mutationRoundCounts):
    initialFitness = fnGetFitness(genes)
    count = random.choice(mutationRoundCounts)
    for i in range(1, count + 2):
        copy = mutationOperators[:]
        func = random.choice(copy)
        while not func(genes):
            copy.remove(func)
            func = random.choice(copy)

        if fnGetFitness(genes) > initialFitness:
            mutationRoundCounts.append(i)
            return


def mutate_add(genes, geneSet):
    index = random.randrange(0, len(genes) + 1) if len(genes) > 0 else 0
    genes[index:index] = random.choice(geneSet)
    return True


def mutate_remove(genes):
    if len(genes) < 1:
        return False
    del genes[random.randrange(0, len(genes))]

    if len(genes) > 1 and random.randint(0, 1) == 1:
        del genes[random.randrange(0, len(genes))]
        return True


def mutate_replace(genes, geneSet):
    if len(genes) < 1:
        return False
    index = random.randrange(0, len(genes))
    genes[index] = random.choice(geneSet)
    return True


def mutate_swap(genes):
    if len(genes) < 2:
        return False
    indexA, indexB = random.sample(range(len(genes)), 2)
    genes[indexA], genes[indexB] = genes[indexB], genes[indexA]
    return True


def mutate_move(genes):
    if len(genes) < 3:
        return False
    start = random.choice(range(len(genes)))
    stop = start + random.randint(1, 2)
    toMove = genes[start:stop]
    genes[start:stop] = []
    index = random.choice(range(len(genes)))
    if index == start:
        index += 1
    genes[index:index] = toMove

    return True


def find_regex(self, wanted, unwanted, expectedLength):
    mutationRoundCounts = [1]
    mutationOperators = [partial(mutate_add, geneSet=fullGeneset),
                         partial(mutate_replace, geneSet=fullGeneset),
                         mutate_remove, mutate_swap, mutate_move]

def fnMutate(genes):
    mutate(genes, fnGetFitness=fnGetFitness, mutationOperators=mutationOperators,)


class RegexTests(unittest.TestCase):
    def test_two_digits(self):
        wanted = {'01', '01', '11', '10'}
        unwanted = ['00', '']

        self.find_regex(wanted, unwanted, 7)

        def find_regex(self, wanted, unwanted, expectedLength,
                       customOperators=None):
            startTime = datetime.datetime.now()
        textGenes = wanted | set(c for w in wanted for c in w)
        fullGeneset = [i for i in allMetas | textGenes]

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes, wanted, unwanted)

        mutationRoundCounts = [1]

        mutationOperators = [
            partial(mutate_add, geneset=fullGeneset),
            partial(mutate_replace, geneset=fullGeneset),
            mutate_remove,
            mutate_swap,
            mutate_move,
        ]
        if customOperators is not None:
            mutationOperators.extend(customOperators)

        def fnMutate(genes):
            mutate(genes, fnGetFitness, mutationOperators,
                   mutationRoundCounts)


    def find_regex(self, wanted, unwanted, expectedLength, customOperators=None):
        startTime = datetime.datetime.now()
        textGenes = wanted | set(c for w in wanted for c in w)
        fullGeneset = [i for i in allMetas | textGenes]


class Fitness:
    UseRegexLength = False

    def __init__(self, numWantedMatched, totalWanted, numUnwantedMatched,
                 length):
        self.NumWantedMatched = numWantedMatched
        self._totalWanted = totalWanted
        self.NumUnwantedMatched = numUnwantedMatched
        self.Length = length

    def __gt__(self, other):
        combined = (self._totalWanted - self.NumWantedMatched) \
                   + self.NumUnwantedMatched
        otherCombined = (other._totalWanted - other.NumWantedMatched) \
                        + other.NumUnwantedMatched
        if combined != otherCombined:
            return combined < otherCombined
        success = combined == 0
        otherSuccess = otherCombined == 0
        if success != otherSuccess:
            return success
        if not success:
            return self.Length <= other.Length if Fitness.UseRegexLength else False
        return self.Length < other.Length

    def __str__(self):
        return "matches: {} wanted, {} unwanted, len {}".format(
            "all" if self._totalWanted == self.NumWantedMatched else self.NumWantedMatched,
            self.NumUnwantedMatched,
            self.Length)


if __name__ == '__main__':
    unittest.main()
