# boj 1076

x = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
A, B, C = [input() for i in range(3)]
result = ((x.index(A) * 10) + x.index(B)) * (10**x.index(C))
print(result)