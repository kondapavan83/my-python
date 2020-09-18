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
            if p(str(i)):
                return(print("{} is a palindrome prime number".format(i)))
                break
            else:
                continue

def p(a):
  for  i  in range(len(a)):
    if a[i]==a[-i-1]:
      t=True
      continue
    else:
      t=False
      break
  return t
