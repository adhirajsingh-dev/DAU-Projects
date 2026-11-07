#MP4 Problem
def issubset(A,B):
    for i in A:
        if i not in B:
            return False
    return True

set_A=set()
set_B=set()
while True:
    a=input('Enter Set A element(or exit to stop):')
    if a.upper()=='EXIT':
        break
    else:
        set_A.add(a)
while True:
    b=input('Enter Set B element(or exit to stop):')
    if b.upper()=='EXIT':
        break
    else:
        set_B.add(b)

subset=issubset(set_A,set_B)
if subset:
    print('A is a subset of B')
else:
    print('A is not a subset of B')


#MP5 Problem
def common_words():
    n=int(input())
    a=set()
    for i in range(n):
        a.add(input())

    m=int(input())
    b=set()
    for i in range(m):
        b.add(input())

    words=set()
    for i in a:
        if i in b:
            words.add(i)

    for word in words:
        print(word)

common_words()
    