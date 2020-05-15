def fibon(m=0,n=5):
     a=1
     b=1
     for i in range(m,n+1):
             yield a
             a,b=b,a+b


for x in fibon(10): print(x)
