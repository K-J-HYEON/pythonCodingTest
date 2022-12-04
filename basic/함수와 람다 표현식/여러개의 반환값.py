def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)