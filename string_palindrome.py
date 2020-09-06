rev=''
print('Enter string to check palindrome :')
str=input()

for i in range((len(str)-1),-1,-1):
    rev=rev+ str[i]

if(rev==str):
    print('String is palindrome.')
else:
    print('String is not palindrome.')
