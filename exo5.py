L1=['e1','e2','e3','e4','e1','e5','e3','e5','e8','e2']
searchedList=[]

count = 0
for index,element in enumerate(L1) :
    elementToSearch = element
    if not(elementToSearch in searchedList) :
        searchedList.append (elementToSearch)
L1 = searchedList
print (L1)