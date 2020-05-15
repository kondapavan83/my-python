def decor(func):
    def do():
        print ('{}'.format('*'*20))
        func()
        print ('{}'.format('*'*20))
    return do
