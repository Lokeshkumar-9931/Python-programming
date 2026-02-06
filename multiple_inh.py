class employee:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"the name is {self.name}")    

class Dancer:
    def __init__(self,dance):
        self.dance=dance
        
    def show(self):
        print(f"the dance form is {self.dance}")   
        
class Danceremployee(employee,Dancer):
    def __init__(self, dance,name):
        self.dance=dance       
        self.name=name

o=Danceremployee("katak","govind")
print(o.name)
print(o.dance) 
o.show() 
print(Danceremployee.mro())      
              