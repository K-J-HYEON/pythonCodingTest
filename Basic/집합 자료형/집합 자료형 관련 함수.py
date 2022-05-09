data = set([1, 2, 3])
print(data)

# 원소 하나 추가
data.add(4)
print(data)

# 원소 여러개 추가
data.update([5, 6])
print(data)

data.remove(3)
print(data)

# 리스트 튜플은 수서가 있어서 인덱싱 통해 자료형의 값 얻는다.
# 하지만 사전 자료형 과 집합 자료형은 수서가 없어서 인덱싱으로 값을 얻을 수 없다.
# 사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.