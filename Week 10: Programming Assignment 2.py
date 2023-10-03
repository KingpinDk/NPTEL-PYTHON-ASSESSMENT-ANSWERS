import math

def closestSchool(x, y, L):
  n = len(L)
  dit={}
  mini = 1000000
  for i in range(n):
    temp=math.sqrt((L[i][0]-x)**2 + (L[i][1]-y)**2)
    mini = min(temp,mini)
    if temp in dit.keys():
      dit[temp].append(L[i])
    else:
      dit[temp]=[]
      dit[temp].append(L[i])
  for key,val in dit.items():
    if(key == mini):
      [print(a) for a in val]
