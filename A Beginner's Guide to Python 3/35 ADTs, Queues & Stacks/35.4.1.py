queue = []  # Create an empty queue.
queue.append('task1')

print("Initial queue: ", queue)

queue.append('task2')
queue.append('task3')
print("queue after additions: ", queue)

element1 = queue.pop(0)
print("element retrieved from queue: ", element1)

print("queue after the pop: ", queue)

element2 = queue.pop()
print("element2 retrieved from queue: ", element2)

print("queue after the pop: ", queue)
