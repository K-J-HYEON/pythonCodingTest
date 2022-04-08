n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1

    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서부터 차근차근 설치
        
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    
    if count >= c:
        start = mid + 1
        result = mid
    
    else:
        end = mid - 1


print(result)