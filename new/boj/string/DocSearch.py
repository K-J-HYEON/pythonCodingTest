# https://www.acmicpc.net/problem/1543
# sol 1
doc = input()
word = input()
res = 0

while True:
    idx = doc.find(word)
    if idx == -1:
        break

    res += 1
    doc = doc[idx+len(word):]

print(res)

# # sol2
# doc = input()
# word = input()
# print(doc.count(word))