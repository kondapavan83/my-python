def hl(x,y=range(0,100)):
    z=y[-1]
    if x< int((z+1)/2):
        if x < int((z+1)/4):
            if x < int((z+1)/8):
                print ("too  small")
            else:
                print ("small")
        else:
            print ("less than half, higher than quarter")
    else:
        if x< int(((z+1)/4)*3):
            print  ("less than 3 quarters")
        else:
            print (" higher than  3  quarters")
