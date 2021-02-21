def Recursion_Multiply(a,b):
    if b == 1:
        return a
    else:
        return a + Recursion_Multiply(a,b-1)


a = int(input('Enter first numbre:'))
b = int(input('Enter second numbre:'))

print(a,'*',b,'=',Recursion_Multiply(a,b))
