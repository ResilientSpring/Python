import random
import datetime
import time

geneSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.'

target = 'Hello World!'

def _generate_parent(length, geneSet):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))

        genes.extend(random.sample(geneSet, sampleSize))
        return ''.join(genes)


def get_fitness(guess):
    return sum([1 for expected, actual in zip(target, guess) if expected == actual])


def _mutate(parent, geneSet):
    index = random.randrange(start=0, stop=len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)


def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print('{}\t{}\t{}'.format(guess, fitness, timeDiff))


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(length=targetLen, geneSet=geneSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    if bestFitness >= optimalFitness:
        return bestParent

    while True:
        child = _mutate(parent=bestParent, geneSet=geneSet)
        childFitness = get_fitness(child)

        if bestFitness >= childFitness:
            continue

        display(child)

        if childFitness >= optimalFitness:
            return child

        bestFitness = childFitness

        bestParent = child



