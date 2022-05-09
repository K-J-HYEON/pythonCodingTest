n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 먼저 500원으로 거슬러주고
    n %= coin

print(count)