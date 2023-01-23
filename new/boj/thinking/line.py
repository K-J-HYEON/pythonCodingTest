# https://www.acmicpc.net/problem/2605

n = int(input())
result = []
st_num = 1
for s in map(int, input().split()):
    result.insert(s, str(st_num))
    st_num += 1

result.reverse()
print(' '.join(result))