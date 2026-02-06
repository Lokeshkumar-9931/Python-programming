class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showdetails(self):
        print(f"the name of the employee is {self.name} \
and its id is {self.id}")
 
class programmer(employee):
    def showlanguage(self):
        print("the default language is python") 
                
emp1=employee("lokesh","2300")
emp1.showdetails()
        
emp2=programmer("shubham","2301")
emp2.showdetails()
emp2.showlanguage()

emp3=employee("krishna","2302")
emp3.showdetails()        