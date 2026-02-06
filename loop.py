for i in range(6):
    print(i)
    if i==4:
        break
else:         # here else will not execute
    print("sorry no I")    
print("\n")    
i=0
while i<7:    
    print(i)
    i+=1    
    if i==4:
        break
else:         #here else will not execute
    print("sorry no I")  

for x in range(5):
    print("iteration no {} in for loop",format(x+1))
else:
    print("else block in loop")    
print("out of loop")              