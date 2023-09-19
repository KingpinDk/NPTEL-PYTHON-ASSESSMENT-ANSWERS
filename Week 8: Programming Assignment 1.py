def squareT(T):
  l = list(T)
  for i in T:
    l.append(i*i)
  return tuple(l)
