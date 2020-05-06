def nrp(x):
  t=0
  n=[]
  for i in range(x,1,-1):
    for j  in range(int(i/2)+1,1,-1):
      if i%j==0:
        t=0
        break
      else:
        t=1
        continue
    if t==1:
      n.append(i)
      break
  for i in range(x,x**10):
    for j  in range(int(i/2)+1,1,-1):
      if i%j==0:
        t=0
        break
      else:
        t=1
        continue
    if t==1:
      n.append(i)
      break
      
  return n
