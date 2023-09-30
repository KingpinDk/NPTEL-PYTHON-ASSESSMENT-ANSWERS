m=max(L)
for i in range(0,m+1):
  if i in L:
    if i ==m:
      print(i,end='')
    else:
      print(i,end=' ')
  else:
    print(0,end=' ')
