def count_letters(S):
  dic = {}
  for i in S:
    if i in dic:
      dic[i]+= 1
    else:
      dic[i] = 1
  
  return dic
