s = input()
count = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]: # 현재 문자와 다음 문자열이 다르면 +1을 해줌
        count += 1

print((count + 1) // 2)