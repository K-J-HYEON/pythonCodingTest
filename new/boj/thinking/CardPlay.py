# https://www.acmicpc.net/problem/2511

A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = 0
b = 0
last_win = 0
for i in range(10):
    if(A[i] > B[i]):
        a += 3
        last_win = 1
    elif (A[i] < B[i]):
        b += 3
        last_win = -1
    else:
        a += 1
        b += 1

print(str(a) + " " + str(b))

if ((a>b) or (b == a and last_win == 1)):
    print("A")
elif ((b > a) or (b == a and last_win == -1)):
    print("B")
else:
    print('D')