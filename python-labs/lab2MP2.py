x=int(input('Enter a number(>2):'))
prime=True
for i in range(2,x):
    if x%i==0:
        prime=False
        a=i
        break
if prime==True:
    print(x,'is a prime')
else:
    print(x,'is not a prime')
    print('A factor of',x,'other than 1 and',x,'is',a)
    