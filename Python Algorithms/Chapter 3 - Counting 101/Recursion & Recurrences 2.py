def T(seq, i=0):
    if i == len(seq): return 1
    return T(seq, i+1) + 1


sequence = "valiant"

print(len(sequence))

print(T(sequence))
