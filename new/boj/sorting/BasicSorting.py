## 시간복잡도 -> 빅오표기법을 고려하면서 계산
## 다른사람 문제 참고 최대 3개블로그 /  최소 유형별로 10~15문제

n = int(input())
word = []

for _ in range(n):
    word.append(input())

word = list(set(word))
word.sort(key=lambda x : (len(x), x))

print("\n".join(word))