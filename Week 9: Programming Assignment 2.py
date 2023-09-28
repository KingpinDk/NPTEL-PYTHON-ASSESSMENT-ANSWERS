def mergeDic(d1, d2):
  for i in d2:
    if i not in d1:
      d1[i]=d2[i]
  return d1
