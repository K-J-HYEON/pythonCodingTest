# n = int(input())
#
# sum = 1
#
# if n > 0:
#     for i in range(n + 1):
#         sum *= i
#
# print(sum)

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))