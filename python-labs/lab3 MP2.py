a=int(input('Enter no of elements you want in the list:'))
lst=[]
new_lst=[]
for i in range(a):
    elem=int(input('Enter element:'))
    lst.append(elem)
print(lst)
for j in lst:
    if j not in new_lst:
        new_lst.append(j)
print(new_lst)