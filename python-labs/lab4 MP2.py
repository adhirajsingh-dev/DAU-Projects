import random
def Digit_To_Int():
    n=int(input('Enter no of digits:'))
    s='0123456789'
    k=random.choice(s[1:])
    for i in range(n-1):
        k=k+random.choice(s)
    print(k)
Digit_To_Int()
