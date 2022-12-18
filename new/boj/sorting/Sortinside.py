N = int(input())
li = []
for i in str(N):
    li.append(i)

li.sort(reverse=True) # 내림차순으로 정렬
print(li)

for i in li:
    print(i, end='')