#fibonacci=0,1,1,2,3,5....



num=int(input("Enter the range :"))
first=0
second=1
for i in range (0,num):
    if(i<=1):
        f=i
    else:
        f=first+second
        first=second
        second=f
    print(f)
    
