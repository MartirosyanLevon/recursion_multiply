def recursion_multiply(a,b):
    if b == 1:
        return a
    else:
        return a + recursion_multiply(a,b-1)


a = int(input('Enter first numbre:'))
b = int(input('Enter second numbre:'))

print(a,'*',b,'=',recursion_multiply(a,b))
