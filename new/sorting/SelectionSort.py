array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]

print(array)

# 파이썬 스와프 소스코드
# array = [3, 5]
# array[0], array[1] = array[1], array[0]
# print(array)

# C 언어로 구현한 스와프 예제
# int a = 3;
# int b = 5;
# # 스와프 진행;
# int temp = a;
# a = b;
# b = temp;