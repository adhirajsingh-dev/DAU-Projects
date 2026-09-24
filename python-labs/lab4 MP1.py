from random import sample
grid=[]
for i in range(6):
    row=[]
    for j in range(6):
        row.append(0)
    grid.append(row)

for row in grid:
    indices=sample(range(6),2)
    for z in indices:
        row[z]=1

for row in grid:
    print(' '.join(str(num) for num in row))
