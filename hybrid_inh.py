class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def making_sound(self):
        print("sound made by the animal")  

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name, species="Dog")    
        self.breed=breed
    def making_sound(self):
        print("!Bark")  

class cat(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name, species="cat")    
        self.breed=breed
    def making_sound(self):
        print("Meow")            


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