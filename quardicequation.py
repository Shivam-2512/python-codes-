import cmath

print(" please enter values of a b & c")
a = int(input())
b=int(input())
c=int(input())

d=(b**2) - (4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('The solution are : '+ str(sol1) + ' and ' +str(sol2))
