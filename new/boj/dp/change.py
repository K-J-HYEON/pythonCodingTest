# 1. 동전은 2원짜리 / 5원짜리밖에 없음 두 동전으로만 거스름돈 줘야함
# 2. 최소한으로 주기 위해 5원짜리로 먼저 한번씩 나눔
# 3. 만약 나누어 떨어지면 5로 나눈 몫이 답이 됨
# 4. 나누어 떨어지지 않으면 2원짜리로 n을 빼주고 5원짜리로 나누어질때까지 반복


n = int(input())
cnt = 0
i = 0
while True:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

    if n < 0:
        break

if n < 0: # 음수면 거슬러줄수 없다다    print(-1)
    print(-1)
else:
    print(cnt)