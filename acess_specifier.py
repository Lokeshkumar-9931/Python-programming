class employee:
    def __init__(self):
        self.__name="lokesh"
        
a=employee()
#print(a.__name) #cannot be acessed directly
print(a._employee__name)#can be accessed  indirectly
print(a.__dir__())

class student:
    def __init__(self):
        self._name="Lokesh" #private
        
    def _funname(self):  #protected method
        return "code with lokesh"

class subject(student):   #inheritance class
  pass 

obj1=student()
obj2=subject()
print(dir(obj1))
        
# call object by student         
print(obj1._name)
print(obj1._funname())  

#call object by student

print(obj2._name)
print(obj2._funname())
  
     