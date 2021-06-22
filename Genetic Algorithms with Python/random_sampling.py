import random
import datetime
import time

geneSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.'

newGene, alternate = random.sample(geneSet, 2)

print(newGene, alternate)

genome = random.sample(geneSet, 4)

print(genome)
