str1='abcdefghijklmnopqrstuvwxyz'
d={}
ts=''
with open('wordlist.txt','r') as f:
    words=f.readlines()
    total=len(words)
    for i in str1:
        per=0
        for w in words:
            if i in w:
                per+=1
        d[i]=str((per/total)*100)+'%'
    print('Percentage of words:-')
    print(d)


    for w in words:
        ts=ts+w[:-1]
    t2=len(ts)
    d2={}
    for c in str1:
        p=ts.count(c)
        d2[c]=str(p/t2*100)+'%'
    print('Percentage of letters:-')
    print(d2)

