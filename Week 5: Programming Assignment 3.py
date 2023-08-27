for i in L:
  if i == 2 or i == 3:
    print(i,end = '')
    break
  elif i != 1:
    val = True
    for j in range(2,i):
      if(i%j == 0):
        val = False
        break
    if(val):
      print(i,end = '')
      break
