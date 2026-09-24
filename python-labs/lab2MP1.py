a=int(input('Enter start value of 1st interval:'))
b=int(input('Enter end value of 1st interval:'))
c=int(input('Enter start value of 2nd interval:'))
d=int(input('Enter end value of 2nd interval:'))
if c>a:
    start_overlap=c
else:
    start_overlap=a

if b>d:
    end_overlap=d
else:
    end_overlap=b

if start_overlap <= end_overlap:
    print([a,b],'and',[c,d],'overlap in the interval',[start_overlap,end_overlap])
else:
    print([a,b],'and',[c,d],'do not overlap')