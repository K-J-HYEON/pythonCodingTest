# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-Python

from itertools import permutations

def solution(numbers):
    prime = set()

    for i in range(len(numbers)):
        number_permutation = permutations(list(numbers), i + 1)
        print(list(map(int, map("".join, number_permutation))))
        numbers_perm_list = map(int, map("".join, number_permutation))
        prime_set = set(numbers_perm_list)
