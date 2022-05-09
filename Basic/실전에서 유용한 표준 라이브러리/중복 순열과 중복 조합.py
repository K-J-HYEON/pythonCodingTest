# from itertools import product

# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2)) # 2개 뽑아 모든 순열 구하기(중복 허용)
# print(result)


from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)