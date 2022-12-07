array = [('바나나', 2)]

def setting(data):
    return data[1]
result = sorted(array, key = setting)
print(result)