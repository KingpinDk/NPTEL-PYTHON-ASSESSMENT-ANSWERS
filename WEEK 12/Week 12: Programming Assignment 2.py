val = input().split(" ")
for i in range(len(val)):
  val[i] = val[i][::-1]
val = sorted(val)
for i in range(len(val)):
  val[i] = val[i][::-1]
print(val,end='')
