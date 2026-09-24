#MP4 Problem
def is_pythonid(s):
    keywords=["False", "await", "else", "import", "pass",
        "None", "break", "except", "in", "raise",
        "True", "class", "finally", "is", "return",
        "and", "continue", "for", "lambda", "try",
        "as", "def", "from", "nonlocal", "while",
        "assert", "del", "global", "not", "with",
        "async", "elif", "if", "or", "yield"]

    if s=='':
        return False
    if len(s)==1:
        if (s.isalpha() or s=='_') and (s not in keywords):
            return True
        else:
            return False

    if s in keywords:
        return False

    last_char=s[-1]
    if last_char.isalpha() or last_char.isdigit() or last_char == "_":
        return is_pythonid(s[:-1])
    else:
        return False

str1=input('Enter a string:')
result=is_pythonid(str1)
if result:
    print('Valid identifier')
else:
    print('Invalid identifier')


#MP5 Problem
def findDet(A):
    n=len(A)
    if n==1:
        return A[0][0]

    if n==2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]

    det=0
    for j in range(n):
        if (j+1)%2!=0:
            sj=1
        else:
            sj=-1

        Aj=[row[:j]+row[j+1:] for row in A[1:]]
        det=det+sj*A[0][j]*findDet(Aj)
    return det

n=int(input('Enter matrix dimension:'))
print('Enter matrix row by row(numbers should be separated by space):')
matrix=[]
for i in range(n):
    row_str=input(f"Row {i + 1}: ").split()
    row=[float(val) for val in row_str]
    matrix.append(row)

det_value=findDet(matrix)
print('Determinant of the matrix is',det_value)
