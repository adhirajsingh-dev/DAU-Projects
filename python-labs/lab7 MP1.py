s=input('Enter a string:')
miss_words=''
with open('wordlist.txt','r') as f:
    if s[len(s)-1]=='.':
        s=s[:len(s)-1]
    str1=s.split()
    words=f.readlines()
    for word in str1:
        word=word+'\n'
        if word not in words:
            miss_words=miss_words+word[:-1]+' '
    if len(miss_words)==0:
        print('All words are correct')
    else:
        print('Misspelled words are:',miss_words)
            

    

