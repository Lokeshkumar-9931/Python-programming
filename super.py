from scipy.__config__ import show

class parent:
    def __init__(self,name,roll,id):
        self.name=name
        self.roll=roll
        self.id=id
        
    def show(self):
        print(f"the name is {self.name} and the roll is {self.roll}\
and the id is {self.id}")
    def marks(self):
        marks=[98,88,97,67,85]
        for mark in marks:
            print(mark,end="\n ")
            
class child(parent):
    def result(self):
        print("this the child class")
        super().show()  
    def show(self):
        print("super keyword is used here")
        super().show()      
    
ch=child("lokesh kumar",27,"2360027")
child.marks(ch)
child.result(ch)
child.show(ch)

class employee:
    def __init__(self,name,id,lang):
        self.name=name
        self.id=id
        self.lang=lang

rohan=employee("rohan das","420","c++")
lokesh=employee("lokesh","2345","pyhon")
print(rohan.name,rohan.lang)
print(lokesh.id,lokesh.name)
        
        
                