n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    
    if m == 0: # m이 0이라면 반복문 탈출
        break

    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기


print(result)
