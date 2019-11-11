dividedBy7=[]
dividedBy5=[]
for i in range(1500,2700):
    if (i%7)==0 :
        dividedBy7.append(i)
    if (i%5)==0 :
        dividedBy5.append(i)
print ('divided by 5',dividedBy5)
print ('divided by 7',dividedBy7)
