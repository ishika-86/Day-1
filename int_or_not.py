def check_int(x):
    if type(x)==int:
        return "It is an integer"
    else:
        return "It is a string"


num = input('Enter a number: ')
print(check_int(num))
