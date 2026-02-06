class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def show(self):
        print(f"the name of animal is {self.name} \
and the species is {self.species}")

class dog(animal):
           def __init__(self, name, breed):
                 animal.__init__(self,name,species="Dog") 
                 self.breed=breed
                 
           def show(self):
                animal.show(self)     
class Goldenretriver(dog):
    def __init__(self, name, color):
         super().__init__(name, breed="golden Retriver")
         self.color=color
         
    def show(self):
        dog.show(self) 
        print(f"color: {self.color}")              
        
o=Goldenretriver("tommy","golden")    
o.show()

dog.show()
print(f"color: {self.color}")