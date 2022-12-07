# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1

        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

# 가게 부품개수 n 입력
n = int(input())

# 가게 전체 부품 번호 공백으로 구분하여 입력
array = list(map(int, input().split()))

# 이진탐색 수행하기 위해 사전에 정렬 수헹
array.sort()

# 손님이 확인 요청한 부품 개수 입력
m = int(input())

# 손님 전체 부품 번호를 공백으로 구분해서 입력
x = list(map(int, inout().split()))


# 손님이 확인 요청한 부품 번호 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')

    # 해당 부품이 존재하는지 확인
    else:
        print('no', end = ' ')
