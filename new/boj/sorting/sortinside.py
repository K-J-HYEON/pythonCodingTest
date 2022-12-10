N = int(input())
A = []
A = list(map(int, str(N)))
A.sort(reverse= True)
for n in A:
    print(n, end="")