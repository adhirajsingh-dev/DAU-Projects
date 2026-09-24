def DigitalRoot():
    n=int(input('Enter a number:'))
    n1=str(n)
    while len(n1)!=1:
        sum=0
        for i in n1:
            sum=sum+int(i)
        n1=str(sum)
    print('Digital root is',int(n1))

DigitalRoot()