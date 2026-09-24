def p_add(d1,d2):
    d={}
    for k in d1:
        d[int(k)]=int(d1[k])
    for k in d2:
         d_key=int(k)
         if d_key in d:
              d[d_key]+=int(d2[k])
         else:
              d[d_key]=int(d2[k])
         
    return d
p1={}
p2={}
print('Enter first polynomial:')
while True:
    key1=input('Enter power(type exit to stop):')
    if key1.lower()=='exit':
        break
    value1=input('Enter coefficient:')
    p1[key1]=value1

print('Enter second polynomial:')
while True:
    key2=input('Enter power(type exit to stop):')
    if key2.lower()=='exit':
            break
    value2=input('Enter coefficient:')
    p2[key2]=value2
p=p_add(p1,p2)
l=list(p.keys())
l.sort()
p_sorted={k:p[k] for k in l}
print(p_sorted)



