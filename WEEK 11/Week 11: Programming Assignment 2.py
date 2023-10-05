st=input().split("#")
st.sort()
for i in range(len(st)-1,-1,-1):
  if(i==0):
    print(st[i],end='')
  else:
    print(st[i],end='#')
