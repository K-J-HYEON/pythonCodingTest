# boj 1934 / 수학 / 최소 공배수 / 유클리드 호제법

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(int(g*(a/g)*(b/g)))