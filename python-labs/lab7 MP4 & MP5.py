#MP4 Problem
str1=input('Enter a word(use asterisks for the letters you do not know):')
str1=str1.strip().lower()
matching_words=[]
f=open('wordlist.txt','r')
words=f.readlines()
for word in words:
    word=word.strip().lower()
    if len(str1)!=len(word):
        continue
    is_match=True
    for i in range(len(str1)):
        if str1[i]!='*' and str1[i]!=word[i]:
            is_match=False
            break

    if is_match:
        matching_words.append(word)

if len(matching_words)!=0:
    print('Matching words are:')
    for word in matching_words:
        print(word)
else:
    print('No matching words found.')

f.close()

#MP5 Problem
words_by_length = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
f=open('wordlist.txt','r')
for word in f:
    word=word.strip().lower()
    l=len(word)
    if l>=1 and l<=8:
        words_by_length[l].append(word)

valid_words=[]
for word in words_by_length[1]:
    valid_words.append(word)

for l in range(2,9):
    level=[]
    for word in words_by_length[l]:
        for i in range(l):
            smaller=word[:i]+word[i+1:]
            if smaller in valid_words:
                level.append(word)
                break
    valid_words=level

valid_words.sort()
print('All eight-letter words with this property are:')
for word in valid_words:
    print(word)

f.close()










