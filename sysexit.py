import sys

while True :
    print('Type "exit" to exit')
    response = input()
    if (response == 'exit'):
        sys.exit()
        print('You have typed '+response)


name= input()
if(name== 'shivam'):
    print('Hi, SHivam')
else:
    print('hi,user')
