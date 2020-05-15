def pal(x):
    i=int(len(x)/2)
    j=0
    while True:
        if  j<=i:
            if x[j]==x[-j-1]:
                j+=1
                continue
            else:
                return False
                break
        else:
            return True
            break
