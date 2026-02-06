def my_generator():
    for i in range(100):
        yield i
        
gen=my_generator()
print(next(gen))  
i=1
while  i<11:
    print(next(gen)) 
    i+=1     
    
def gen():
    for j in range(100):
        yield j

gena=gen()
print(next(gena))    
j=1
while j<11:
    print(next(gena))
    j+=1 
   
            