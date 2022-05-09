array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i * j
        print(temp)


# 시간 복잡도 O(N2)
# 참고로 모든 2중 반복문의 시간 복잡도가 O(N2)은 아님
# 소스코드가 내부적으로 다른 함수를 호출하면 그 함수의 시간 복잡도도 고려해야함 