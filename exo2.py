L1=['el1','el2','el3','el4','el5','el6','el7','el8']

indexToRemove = 4
positionToAdd = 2

elToRemove = L1[indexToRemove]
print(elToRemove)
del L1[indexToRemove]

L1.insert(positionToAdd,elToRemove)
L1.append(elToRemove)
print(L1)