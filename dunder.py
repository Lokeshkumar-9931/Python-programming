class employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i 
    def __str__(self):
         return f"the name is employee is {self.name}"
    
    def __repr__(self):
        return f"the name is employee is {self.name} repr"
    
    def __call__(self, *args, **kwds):
        sum=args+(56,)
        a={"name":"lokesh","roll":34}
        print(sum)
        print(a)
        return sum
        
  
