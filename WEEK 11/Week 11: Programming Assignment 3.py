def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return True
  return False
a=int(input())
b=int(input())
for i in range(a,b+1):
  if(i == 0 or i == 1):
    pass
  elif(is_prime(i)):
    print(i)
