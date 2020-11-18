def sums_in_sequence(sequence):
    sums = []
    for seq in sequence:
        sums.append(sum(seq))
    return sums


sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print(sums_in_sequence(sequence))