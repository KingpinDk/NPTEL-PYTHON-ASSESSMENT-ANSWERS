N=list(str(n))
P=[]
for isp in N:
  if isp not in P:
    P.append(isp)
ans=[]
for i in range(len(P)):
  a=[]
  for j in range(len(N)):
    if(P[i]==N[j]):
      a.append(j)
  ans.append(a)

for i in range(len(P)):
  print(int(P[i]), "",end="")
  for j in range(len(ans[i])):
               print(int(ans[i][j]),"",end="")
  print()
