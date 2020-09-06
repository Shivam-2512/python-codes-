'''simple interest
si= pxtxr / 100
p=amount ,r =rate ,t= time'''

#ques = p =10000 r=5 t=5 year find the simple interest

def simple_interest(p,t,r):
    print("The amount is : ", p)
    print("The Given rate is : ", r)
    print("The time span is :", t)

    si=(p*r*t)/100
    print("the simple interest of given values is ",si)
simple_interest(10000,5,5)
