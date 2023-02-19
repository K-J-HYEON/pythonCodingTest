A, B = map(int, input().split())
aList = set(map(int, input().split()))
bList = set(map(int, input().split()))

res = aList - bList

if res:
    print(len(res))
    print(*sorted(list(res)))

else:
    print(0)