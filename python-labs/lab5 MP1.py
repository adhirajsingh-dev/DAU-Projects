l=[]
while True:
    elem=input('Enter integer:')
    if elem.lower()=='done':
        break
    l.append(elem)

def find_min_max(lst):
    if lst==[]:
        return 'null','null'
    if len(lst)==1:
        return lst[0],lst[0]

    smaller,larger=find_min_max(lst[1:])
    if lst[0]<smaller:
        min1=lst[0]
    else:
        min1=smaller
    if lst[0]>larger:
        max1=lst[0]
    else:
        max1=larger
    return min1,max1

min_val,max_val=find_min_max(l)
print(min_val,max_val)

