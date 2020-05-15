class cylinder(object):
    import math
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius
    def vol(self):
        return math.pi*self.radius**2*self.height
    def surf(self):
        return self.height*self.radius
    def __str__(self):
        return f"volume of cylinder  is  {self.vol()} and  surface area is {self.surf()}"
    def  __len__(self):
        return self.height
    def __del__(self):
        print("cylinder object is delted")
