def hist(s):
    d={ch:s.count(ch)*'*' for ch in s}
    for k in d:
        print(k,d[k])

str1=input('Enter a word:')
hist(str1)