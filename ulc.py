def ulcount(x):
    up=0
    low=0
    for i in x:
        if i.upper()==i:
            up+=1
        else:
            low+=1
    print ("# of  lower chars is {l}, while upper is {u}".format(l=low,u=up))
