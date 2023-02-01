# https://comdoc.tistory.com/entry/33-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98%EC%97%B4%EA%B3%BC-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D

fibo = [0 for i in range(50)]
fibo[0] = 0
fibo[1] = 1

n = int(input())
for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])

