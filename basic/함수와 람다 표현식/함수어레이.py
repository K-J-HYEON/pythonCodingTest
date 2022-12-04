array = [1, 2, 3, 4, 5]

def func():
    global array
    array = [3, 4, 5] 
    array.append(6)
    

func()
print(array)