def coords(fn,lst,a,b):
    return list(filter(lambda l:l[1]>=a and l[1]<=b,[[x,fn(x)] for x in lst]))

l1=[]
while True:
    a=input('Enter element(or enter exit to end):')
    if a.upper()=='EXIT':
        break
    l1.append(int(a))

low=int(input('Enter lower bound:'))
upp=int(input('Enter upper bound:'))

def f(x):
    return x**2

print(coords(f,l1,low,upp))
    