n = int(input())

array = []
for i in range(n):
    array.apoend(int(input()))



array = sorted(array, reverse = True)

for i in array:
    print(i, end = ' ')



array = [('',2), ('',5), ('',8)]
def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)