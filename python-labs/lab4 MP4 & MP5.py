#MP4 Problem
def merge():
    c=0
    d=0
    lst1=[]
    lst2=[]
    lst_merged=[]
    a=int(input('Enter no of elements in first sorted list:'))
    for i in range(a):
        a1=int(input('Enter element:'))
        lst1.append(a1)
    b=int(input('Enter no of elements in second sorted list:'))
    for j in range(b):
        b1=int(input('Enter element:'))
        lst2.append(b1)
    while c<len(lst1) and d<len(lst2):
        if lst1[c]<lst2[d]:
            lst_merged.append(lst1[c])
            c+=1
        else:
            lst_merged.append(lst2[d])
            d+=1

    while c<len(lst1):
        lst_merged.append(lst1[c])
        c+=1
    while d<len(lst2):
        lst_merged.append(lst2[d])
        d+=1

    print('The sorted merged list is',lst_merged)

merge()

#MP5 Problem
import random
grid=[]
for i in range(5):
    row=random.choices(['M','0'],k=5)
    grid.append(row)

print('Initial Grid')
for row in grid:
    print(' '.join(row))
result=[["" for _ in range(5)] for _ in range(5)]
for r in range(5):
    for c in range(5):
        if grid[r][c] == 'M':
            result[r][c] = 'M'
        else:
            row_start = max(0, r - 1)
            row_end = min(5, r + 2)
            col_start = max(0, c - 1)
            col_end = min(5, c + 2)

            mine_count = sum(row[col_start:col_end].count('M') for row in grid[row_start:row_end])
            result[r][c] = str(mine_count)

print()
print('Final Grid')
for row in result:
    print(' '.join(row))

