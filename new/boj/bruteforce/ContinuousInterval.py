# boj 2399
# https://melonicedlatte.com/algorithm/2020/03/31/191300.html

from sys import stdin
sum = 0
N = int(stdin.readline())
x_list = list(map(int, stdin.readline().split()))
for i, x in enumerate(x_list):
    for y in x_list[i+1]:
        sum += abs(x - y)
    print(sum * 2)