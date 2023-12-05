import math

n = int(input())

discounts = {
    "1": 0.3,
    "2": 0.2,
    "3": 0.15,
    "4": 0.1,
}

for i in range(n):
    price, level, has_coupon, payment = input().split()
    price = float(price)

    if level in discounts:
        discount = discounts[level]
        price *= (1 - discount)

    if has_coupon == "O":
        price *= 0.95

    if payment == "C":
        price = math.floor(price)
    elif payment == "P":
        price = round(price, 2)

    print(f"{price:.2f}")
