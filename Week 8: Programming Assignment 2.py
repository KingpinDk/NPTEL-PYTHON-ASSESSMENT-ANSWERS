def isVowel(c):
  c = c.lower()
  if(c == 'a' or c== 'e' or c == 'i' or c == 'o' or c == 'u'):
  	return True;
  else:
  	return False;
def replaceV(S):
  L = list(S)
  for i in range(0,len(S)-2):
    if(isVowel(L[i]) and isVowel(L[i+1]) and isVowel(L[i+2])):
      L[i] = '#'
      L[i+1] = '#'
      L[i+2] = '#'
      i+=2
  return ("".join(L).replace("###","_"))
