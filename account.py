class  Account(object):
    def __init__(self,owner,num,bal):
        self.owner=owner
        self.num=num
        self.bal=bal
    def  add(self,val):
        self.bal=self.bal+val
        print (f"current balance after  adding is {self.bal}")
    def deduct(self,val):
        if self.bal-val >= 0:
            self.bal=self.bal-val
            print (f"current balance after  deducting is {self.bal}")
        else:
            print ("sorry not enough funds for this withdrawal")
    def __str__(self):
        return f"Account number {self.num}  is owned  by {self.owner} and the current balance is {self.bal}"
    def __del__(self):
        print("Account has  been deleted")
