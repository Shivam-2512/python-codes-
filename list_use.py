NameFolder=[]
a=0
print('Please start entering the names of students : ')
print()

while True:
    print('Enter the name of student '+str(a+1))
    name=input()
    if(name=='exit'):
        print('Thank you')
        print()
        break
    else:
        NameFolder=NameFolder+[name]
        a=a+1

print('the names of the students are : ')
print()
for i in range(len(NameFolder)):
    print(NameFolder[i])
