# boj 1173 운동

# N, m, M, T, R
# N = 시간 / m 초기맥박 / R => 휴식 선택 맥박이 R 만큼 감소
# m + T <= M에만 운동 가능 ///// m - R < m => 영식이 맥박 = m
# R = > 휴식 선택하는 경우 맥박이 R 만큼 감소

import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, sys.stdin.readline().split())
minute, ex_minute = 0, 0
pulse = m

while ex_minute < N:
    if m + T > M:
        break
    # 운동
    if pulse + T <= M:
        pulse += T
        ex_minute += 1
    else:
        pulse = max(pulse - R, m)

    minute += 1
print(minute if ex_minute == N else -1)

