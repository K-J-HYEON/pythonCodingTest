import sys

lst = []
for i in range(26):
    lst.append(chr(i+97))

plain_text = sys.stdin.readline().rstrip()
s_key = sys.stdin.readline().rstrip()

s_key2 = ''
while True:
    if len(s_key2) > len(plain_text):
        break
    else:
        s_key2 += s_key

v1 = 0
lsta = []
for i in range(len(plain_text)):
    try:
        v1 = lst.index(plain_text[i]) - lst.index(s_key2[i])
        if v1 > 0:
            lsta.append(lst[v1-1])
        elif v1 <= 0:
            lsta.append(lst[v1-1])
    except ValueError:
        lsta.append(" ")
print(''.join(lsta))