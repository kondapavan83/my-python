def p(a):
  for  i  in range(len(a)):
    if a[i]==a[-i-1]:
      tmp=True
      continue
    else:
      tmp=False
      break
  if tmp==True:
    return(print("{} is a palindrome".format(a)))
  else:
    return(print("{} is \"NOT\" a palindrome".format(a)))
