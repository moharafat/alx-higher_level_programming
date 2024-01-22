def divide(a, b):
    if b == 0:
        raise ZeroDivisionError ("Divide by zero")
    return a / b
res = divide(5, 0)
print (res)