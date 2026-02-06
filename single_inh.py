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
        
d=dog("tommy","pitbull")
d.making_sound()        
a=animal("jack","ox")
a.making_sound()
c=cat("pussy","cat")
c.making_sound()
print(d.name)
print(d.breed)
print(d.making_sound())