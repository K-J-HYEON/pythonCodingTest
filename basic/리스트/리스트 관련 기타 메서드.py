# 시간복잡도 O(~)

# append() => O(1)

# sort() / sort(reverse = True) => O(NLogN)

# reverse() => O(N)

# insert(삽입할 위치 인덱스, 삽입할 값) => O(N)

# 변수명.count(특정 값) => O(N)

# 변수명.remove(특정 값) => O(N)

a = [1, 4, 3]
print(a)

a.append(2)
print("삽입: ", a)

a.sort()
print("오름차순 정렬: ", a)

a.sort(reverse = True)
print("내림차순 정렬: ", a)


a.reverse()
print("원소 뒤집기: ", a)

a.insert(2, 10)
print("인덱스 2에 10 추ㄱㅏ: ", a)

print("개수", a.count(3))

a.remove(1)
print("값이 1인 데이터", a)