list=[5,1,0,1,2,555,1111,-10]
max = list[0]
for i in range(len(list)):
    if max < list[i]:
        max = list[i]

print('largest num is :'+ str(max))
