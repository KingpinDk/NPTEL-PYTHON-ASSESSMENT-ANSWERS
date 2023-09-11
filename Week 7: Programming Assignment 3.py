def snake(M): 
  sk=0 
  sm=[] 
  for r in M: 
    m=[] 
    sk=sk+1 
    if sk%2==0: 
      m=r[::-1] 
    else: 
      m=r 
    sm+=m 
  return(sm) 
