def uniqueE(L):
  L.sort()
  d ={}
  
  for i in L:
    if(i in d):
      d[i] += 1
    else:
      d[i] = 1
  L.clear()
  for i in d:
    if(d[i]==1):
      L.append(i)
  return L
