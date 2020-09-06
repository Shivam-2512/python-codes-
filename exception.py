def divide(a):
    try :
        return(27/a)
    except ZeroDivisionError :
        print("Invalid, can't divide by zero")

print(divide(3))
print(divide(0))
print(divide(2))
