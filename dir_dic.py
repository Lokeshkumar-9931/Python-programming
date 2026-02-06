#dir  __dic__  help
x=[12,23,34]
print(dir(x)) #it shows all the methods
print(x.__add__)

x=(12,23,34)
print(dir(x))
print(x.__add__)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
p=person("lokesh",23)
print(p.__dict__)        #it shows the key-value pair form of object and class
print(help(person))