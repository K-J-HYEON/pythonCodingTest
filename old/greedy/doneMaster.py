n = 1260

count = 0

coin_types = []

for coin in coin_types:
    count += n // coin
    n %= coin


print(count)