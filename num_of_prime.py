def nop(x):
  n=[]
  for i in range(x,1,-1):
    for j  in range(int(i/2)+1,1,-1):
      if i%j==0:
        tmp=0
        break
      else:
        tmp=1
        continue
    if tmp==True:
      n.append(i)
  return len(n)
