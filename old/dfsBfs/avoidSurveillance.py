from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
# 장애물 설치할 수 있는 위치 저장(빈 공간)
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    # 왼쪽방향
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False    
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if direction == 3:
        while x <= n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    
    return False


# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 한개씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True

    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

for data in combination(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break

    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')

else:
    print('NO')