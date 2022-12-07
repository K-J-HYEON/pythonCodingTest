# 북쪽은 행을 -1 남쪽은 행을 +1
dx = [0, -1, 0, 1]
# 서쪽은 열을 -1 동쪽은 열을 + 1
dy = [1, 0, -1, 0]

x, y = 2, 2 

# 동 북 서 남

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)