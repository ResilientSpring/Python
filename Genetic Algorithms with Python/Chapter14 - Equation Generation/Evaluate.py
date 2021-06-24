def evaluate(genes):
    result = genes[0]
    for i in range(1, len(genes), 2):
        operation = genes[i]
        nextValue = genes[i + 1]
        if operation == '+':
            result += nextValue
        elif operation == '-':
            result -= nextValue
    return result


def get_fitness(genes, expectedTotal):
    result =  evaluate(genes)

    if result != expectedTotal:
        fitness = expectedTotal - abs(result - expectedTotal)
    else:
        fitness = 1000 - len(genes)

    return fitness