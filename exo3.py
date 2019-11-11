L1=['e1','e2','e3','e4','e5','e6','e7','e8']
Result =[]
NoOfChunk = 3
ListLength = len(L1)
#compute chunk length. Need to round up.
ChunkLength = -(-(ListLength)//NoOfChunk)
print (ChunkLength)
#take 3 chunk from the list
StartChunck=0
EndChunk=ChunkLength
for i in range(NoOfChunk):
    #create new list
    if (EndChunk) < len (L1) :
        ListToAdd=(L1[StartChunck:EndChunk])
    else :
        ListToAdd=(L1[StartChunck:len(L1)])
    ListToAdd.reverse()
    Result.append(ListToAdd)
    StartChunck=StartChunck+ChunkLength
    EndChunk=EndChunk+ChunkLength
print (Result)

