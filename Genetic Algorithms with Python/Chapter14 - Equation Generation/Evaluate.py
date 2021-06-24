def evaluate(genes):
    result = genes[0]
    for i in range(1, len(genes), 2):
        operation = genes[i]
        nextValue = genes[i + 1]
        if operation == '+':
            result += nextValue