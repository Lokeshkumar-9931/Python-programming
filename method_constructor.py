class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
      
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])   
        
e=employee("Lokesh",12000)
print(e.name)
print(e.salary)
string="Harry-12000" 
e2=employee.fromstr(string)    
print(e2.name)
print(e2.salary)
        
        