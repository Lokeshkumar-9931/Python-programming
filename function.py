a=9
b=87
gmean=(a*b)/(a+b)
print(gmean)

def calc_gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
calc_gmean(4,5) 
calc_gmean(67,4)  
print("\n")

def find_large(a,b):
    if(a>b):
        print("greater is a")
    else:
        print("greater is b")    

a=34
b=35
calc_gmean(a,b)
find_large(a,b)    

def average(a=9,b=8):
    print("avg is",(a+b)/2)
average(76)    
average(b=23)    
average()    
average(23,76)     
 
def avg(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=avg(5,7,8)
print(c)  

def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])
name(mname="bacchan",lname="panday",fname="lokesh")           