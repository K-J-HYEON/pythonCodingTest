import sys
input = sys.stdin.readline

N = int(input()) # 대회참가 학생 수

students = []

for _ in range(N):
    students.append(list(map(int, input().split())))

students = sorted(students, key = lambda x : -x[2])

# 참가국이 같을 경우 1,2,4등 출력
if students[0][0] == students[1][0]:
    print(*students[0][:2])
    print(*students[1][:2])
    print(*students[3][:2])

else: # 참가국이 다를 경우 1, 2, 3등 출력
    print(*students[0][:2])
    print(*students[1][:2])
    print(*students[2][:2])