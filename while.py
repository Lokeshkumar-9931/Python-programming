for i in range(0,17):
    print(i,end=" ")
print("\n")

i=0
while(i<=10):
    print(i)    
    i+=1    
    
s=10
while(s>0):
    print(s)
    s-=1   
else:
    print("i am in else")   

for i in range(1,11):
    print("5 x",i,"=",5*i)          
    if(i==11):
       break
else:
    print("your table is ready")
print("\n")    
    
i=1
while True:   
    print(i)
    i+=1
    if(i%100==0):
        break  

for i in range(1,11):         
    if(i==3):
       continue
    print("5 x",i,"=",5*i) 
else:
    print("your table is ready")     