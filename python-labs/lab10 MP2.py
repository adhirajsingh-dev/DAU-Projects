def add_matrices(x,y):
    return [[sum(pair) for pair in zip(x[i],y[i])] for i in range(len(x))]
    
def build_matrix():
    r=int(input('Enter no. of rows:'))
    c=int(input('Enter no. of columns:'))
    matrix=[]
    for i in range(r):
        row=[]
        print('Enter for row',i+1)
        for j in range(c):
            elem=int(input('Enter element:'))
            row.append(elem)
        matrix.append(row)
    return matrix
l1=build_matrix()
l2=build_matrix()
print(add_matrices(l1,l2))

