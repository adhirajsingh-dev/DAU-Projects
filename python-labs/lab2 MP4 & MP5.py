#MP4 Problem
a=input('Enter a word:')
vowels='aeiouAEIOU'
for i in range(len(a)):
    if a[i] in vowels:
        b=a[i]
        a=a[:i+1]+'lf'+b+a[i+1:]
        break
print(a)


#MP5 Problem
word=input('Enter an LF word:')
vowels='aeiouAEIOU'
for i in range(len(word)-2):
    if word[i] in vowels and word[i+1:i+3].lower()=='lf' and word[i+3]==word[i]:
        word=word[:i+1]+word[i+4:]
        break
print(word)



