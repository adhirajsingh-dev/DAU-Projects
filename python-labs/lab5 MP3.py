def base_conversion(num,base):
    if num<base:
        print(num,end=' ')
        return
    base_conversion(num//base,base)
    print(num%base,end=' ')

a=int(input('Enter number:'))
b=int(input('Enter base:'))
if b<2:
    print('Invalid base')
else:
    base_conversion(a,b)