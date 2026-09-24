a=int(input('Enter no of elements you want in the list:'))
lst=[]
for i in range(a):
    elem=input('Enter element:')
    lst.append(elem)
l=len(lst)
if lst:
    last_elem = lst[-1]
    for j in range(l-1, 0, -1):
        lst[j] = lst[j - 1]
    lst[0]=last_elem
print(lst)
