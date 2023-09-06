def snake(M):
  L = []
  n = len(M)
  for i in range(0,n):
    if(i%2 == 0):
        for j in range(0,n):
            L.append(M[i][j])
    else:
        for j in range(n-1,-1,-1):
            L.append(M[i][j])
  return L
