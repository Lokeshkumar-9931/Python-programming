a=(input("enter the number: "))
print(f"multiplication table of {a} is: ")
try:
    for i in range(1,11):
     print(f"{int(a)} x {i} = {int(a*i)}")
except Exception as e:
    print("sorry the entered value is wrong")

print("end line of code")    

try:
    num=int(input("enter a number: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("number entered is not an integer")    
except IndexError:
    print("index error")  
print("\n")

def func1():
    try:
      l=[1,3,5,7,9]      
      i=int(input("enter a index: "))
      print(l[i])
      return 1
    except:
      print("some error occurred")   
      return 0

    finally:
      print("i am always executed ") 
#print("i am always executed ")        

x=func1()
print(x)   

print("\n") 
# raise error

a=(input("enter the number: "))

if(int(a)<5 or int(a)>9):
    raise ValueError("value should be betwwen 5 and 9")
elif((a)=="QUIT" or "quit"):
    print("don't worry")
    