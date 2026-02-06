a=True
print(a:=False)

numbers=[23,43,54,67]
while (n:=len(numbers)) > 0:
    print(numbers.pop())
    print(numbers)
    
foods=list()
while True:
    food=input("what food do you like?: ")
    if food =="quit":
            break
    foods.append(food)
print(foods) 

cooks=list()
while(cook:=input("what food do you like?: ")) !="quit":
    cooks.append(cook) 
print(cooks)  
        