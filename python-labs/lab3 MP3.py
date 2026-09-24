phone_no=input('Enter a phone number:')
lst=phone_no.split('-')
a='1234567890-'
found=True
for i in phone_no:
    if i not in a:
        print('Invalid')
        found=False
        break
if found==True:
    if lst[0]=='1' and len(lst)==4:
        if len(lst[1])==3 and len(lst[2])==3 and len(lst[3])==4:
            print('Valid')
        else:
            print('Invalid')
    else:
        if len(lst)==3:
            if len(lst[0])==3 and len(lst[1])==3 and len(lst[2])==4:
                print('Valid')
            else:
                print('Invalid')
        else:
            print('Invalid')
