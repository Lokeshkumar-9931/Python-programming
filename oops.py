class Person:
    name="lokesh"
    occupation="software engineer"
    networth=10
    def info(self):
        print(f"{self.name} is {self.occupation} and the networth is {self.networth}")
a=Person()
b=Person()
a.name="shubham"
a.occupation="accountant"
a.networth="10000000" 
b.name="sweta"
b.occupation="housewife"
b.networth="12345678"
print(a.name,a.occupation)   
a.info()    
b.info()

#constructor
class person:
    def __init__(self,n,o):
        print("hey I am a person")
        self.name=n
        self.occ=o
    def info(self): 
      print(f"{self.name} is a {self.occ}")

a=person("lokesh","developer")
b=person("ravan","king")
print(a.name)
print(b.name)
print(a.name)
a.name="Divya"
a.occ="HR"
a.info()  
b.info()  