def is_palindrome(s):
    if s=='' or len(s)==1:
        return 'It is a palindrome'
    
    if s[0]==s[len(s)-1]:
        return is_palindrome(s[1:len(s)-1])
    else:
        return 'It is not a palindrome'

str1=input('Enter a string:')
str2=''
for i in str1:
    if i.isalpha():
        str2=str2+i
print(is_palindrome(str2.upper()))
