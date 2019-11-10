L1 = ['el1.1','el1.2','el1.3','el1.4']
L2 = ['el2.1','el2.2','el2.3','el2.4']
L3 =[]
for index,element in enumerate(L1):
    if index%2 == 0 :
      L3.append(L1[index])
    else :
      L3.append(L2[index])
print ("Hello")
print (L3)
