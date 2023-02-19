# https://www.acmicpc.net/problem/11478

S = input()
string = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        string.add(S[i:j+1])

print(len(string))