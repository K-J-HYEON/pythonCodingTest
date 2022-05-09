a = 0

def func():
    global a
    a += 1
    

for i in range(10):
    func()

print(a)



# bullshit dont use
# a = 10

# def func():
#     a += 1