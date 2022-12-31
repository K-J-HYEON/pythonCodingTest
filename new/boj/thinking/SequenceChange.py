# boj 1551

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = list(map(int, input().split(',')))

temp = []

for method_index in range(k):
    for sequence_index in range(len(sequence) - 1):
        temp.append(sequence[sequence_index + 1] - sequence[sequence_index])

    sequence = temp
    temp = []

sequence = list(map(str, sequence))

print(','.join(sequence))
