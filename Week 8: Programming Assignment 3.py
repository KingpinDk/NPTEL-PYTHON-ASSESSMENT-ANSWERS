i = -1
for j in range(0,len(L)):
  if(L[j] != 0):
    i+=1
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
print(L,end='')
  
