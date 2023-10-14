val = input()
for i in val:
  if(i == '@'):
    print(" ",end='')
  elif(i == '.'):
    break
  else:
    print(i,end='')
