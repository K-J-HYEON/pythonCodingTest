data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'banana'
data['코코넛'] = 'Coconut'

key_list = list(data.keys())
value_list = list(data.values())
print(key_list)
print(value_list)

for key in key_list:
    print(data[key]) 


a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {

    '홍길동' : 97,
    '이말년' : 100
}
print(b)

print(b['이말년'])

key_list = list(b.keys())
print(key_list)