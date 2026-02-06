# instance vs class variable
class employee:
    companyname="apple"      #class variable
    NoOfEmployees=0
    def __init__(self,name): #instance
        self.name=name
        self.raise_amount=0.02
        employee.NoOfEmployees +=1
    def showdetails(self):
        print(f"the name of employee is {self.name} \
and the raise amount is {self.raise_amount} \
and the company name is {self.companyname} \
number of employees in company is {self.NoOfEmployees}")    
        
emp1=employee("lokesh")
emp1.raise_amount=0.04  
emp1.companyname="Apple india"   #instance has more priority
emp1.showdetails()

# employee.showdetails(emp1)   
emp2=employee("Rohan")     
emp2.showdetails()
        
        
        
        
        
        