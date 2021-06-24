import unittest
import datetime
import circuits
import random


def display(candidate, startTime):
    circuit = nodes_to_circuit(nodes=candidate.Genes)
    timeDiff = datetime.datetime.now() - startTime

    print('{}\t{}\t{}'.format(circuit, candidate.Fitness, timeDiff))


def create_gene(index, geneSet):
    gateType = random.choice(geneSet)
    indexA = indexB = None

    if gateType[1].input_count() > 0:
        indexA = random.randint(a=0, b=index)

    if gateType[1].input_count() > 1:
        indexB = random.randint(a=0, b=index)
        if indexB == indexA:
            indexB = random.randint(a=0, b=index)
    return Node(gateType[0], indexA, indexB)


class Node:
    def __init__(self, createGate, indexA=None, indexB=None):
        self.CreateGate = createGate
        self.IndexA = indexA
        self.IndexB = indexB


def nodes_to_circuit(nodes):
    circuit = []

    usedIndexes = []

    for i, node in enumerate(nodes):
        used = {i}

        inputA = circuit[node.IndexA] if node.IndexA is not None \
                                         and i > node.IndexA else None

        if inputA != None:
            used.update(usedIndexes[node.IndexA])

        inputB = circuit[node.IndexB] if node.IndexB is not None \
                                         and i > node.IndexB else None

        circuit.append(node.CreateGate(inputA, inputB))

    return circuit[-1]


def get_fitness(genes, rules, inputs):
    circuit = nodes_to_circuit(genes)
    sourceLabels = 'AB'
    rulesPassed = 0

    for rule in rules:
        inputs.clear()
        inputs.update(zip(sourceLabels, rule[0]))
        if circuit.get_output() == rule[1]:
            rulesPassed += 1
    return rulesPassed


class CircuitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.inputs = dict()

        cls.geneSet = [[circuits.And, circuits.And],
                       [lambda i1, i2: circuits.Not(i1), circuits.Not],
                       [lambda i1, i2: circuits.Source('A', cls.inputs), circuits.Source],
                       [lambda i1, i2: circuits.Source('B', cls.inputs), circuits.Source]]

    def test_generate_OR(self):
        rules = [
            [[False, False], False],
            [[False, True], True],
            [[True, False], True],
            [[True, True], True]
        ]

        self.find_circuit(rules=rules, expectedLength=optimalLength)

    def find_circuit(self, rules, expectedLength):
        startTime = datetime.datetime.now()

        def fnDisplay(candidate, length=None):
            if length is not None:
                print("-- distinct nodes in circuit:",
                      len(nodes_to_circuit(candidate.Genes)[1]))

            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes, rules, self.inputs)

        def fnCreateGene(index):
            return create_gene(index, self.geneSet)

        def fnMutate(genes):
            mutate(genes, fnCreateGene)

        maxLength = 50

        def fnCreate():
            return [fnCreateGene(i) for i in range(maxLength)]

        def fnOptimizationFunction(variableLength):
            nonlocal maxLength
            maxLength = variableLength
            return genetic.get_best(fnGetFitness, None, len(rules), None,
                                    fnDisplay, fnMutate, fnCreate,
                                    poolSize=3, maxSeconds=30)

        def fnIsImprovement(currentBest, child):
            return child.Fitness == len(rules) and \
                   len(nodes_to_circuit(child.Genes)[1]) < \
                   len(nodes_to_circuit(currentBest.Genes)[1])

        def fnIsOptimal(child):
            return child.Fitness == len(rules) and \
                   len(nodes_to_circuit(child.Genes)[1]) <= expectedLength

        def fnGetNextFeatureValue(currentBest):
            return len(nodes_to_circuit(currentBest.Genes)[1])

        best = genetic.hill_climbing(fnOptimizationFunction,
                                     fnIsImprovement, fnIsOptimal,
                                     fnGetNextFeatureValue, fnDisplay,
                                     maxLength)
        self.assertTrue(best.Fitness == len(rules))
        self.assertFalse(len(nodes_to_circuit(best.Genes)[1])
                         > expectedLength)
