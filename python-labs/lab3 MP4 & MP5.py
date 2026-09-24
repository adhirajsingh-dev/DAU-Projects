#MP4 Problem
import random
lst=[]
max_zero=0
current_zero=0
for i in range(100):
    lst.append(random.randint(0,1))
for j in lst:
    if j==0:
        current_zero+=1
        if current_zero>max_zero:
            max_zero=current_zero
    else:
        current_zero=0
print(lst)
print('Longest run of zeros is',max_zero)

#MP5 Problem
import string
import random
all_chars=string.ascii_letters+string.digits+string.punctuation
grid_chars=random.sample(all_chars,18)*2
random.shuffle(grid_chars)
grid=[]
index=0
for i in range(6):
    row=[]
    for j in range(6):
        row.append(grid_chars[index])
        index+=1
    grid.append(row)

for row in grid:
    print(' '.join(row))




        
