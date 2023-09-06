def DiagCalc(M):
  n = len(M)
  m = len(M[0])
  val1 = 0
  val2 = 0
  for i in range(0,n):
    for j in range(0,m):
      if(i==j):
        val1+=M[i][j]
      if(i+j == n-1):
        val2+=M[i][j]
  print(val1)
  print(val2, end='')
