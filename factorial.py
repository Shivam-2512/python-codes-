#4!=4x3x2x1
fac=1

print("Enter the number to calculate it's factorial.")
num = int(input())
for i in range(1,num+1):
    fac=fac*i

print("Factorial of the given num is : ",fac)
