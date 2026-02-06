class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y 
 
class circle(shape):
    def __init__(self, radius):
        self.radius=radius  
        super().__init__(radius,radius)  #method overriding   
        
    def area(self):
        return 3.14* super().area()  
rec=shape(34,2)
print(rec.area())
cir=circle(34)
print(cir.area())

class cir():
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*(self.radius**2)
c=cir(5)
print(c.area())        
        
        