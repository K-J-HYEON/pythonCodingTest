data = input()

result = int(data[0])


for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0 혹은 1인경우 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num


print(result)