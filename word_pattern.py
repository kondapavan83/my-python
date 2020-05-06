>>> def wp(p,x):
...     for i in range(len(list(zip(p,x.split())))):
...             for j in range(len(list(zip(p,x.split())))-i):
...                     if (list(zip(p,x.split()))[i][0]==list(zip(p,x.split()))[i+j][0]) and (list(zip(p,x.split()))[i][1]==list(zip(p,x.split()))[i+j][1]):
...                             continue
...                     if (list(zip(p,x.split()))[i][0]!=list(zip(p,x.split()))[i+j][0]) and (list(zip(p,x.split()))[i][1]!=list(zip(p,x.split()))[i+j][1]):
...                             continue
...                     else:
...                             return False
...                             break
...             return True
...
>>> wp(p,x)
False
>>> x='there are are there'
>>> wp(p,x)
True
>>> x='there are are are'
>>> wp(p,x)
False
>>> p
'abba'
>>> x
'there are are are'
>>>
