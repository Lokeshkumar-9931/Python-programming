#time module
import time
def usingwhile():
    i=0
    while i<5:       
        i=i+1
        print(i)
        
def usingfor():
    for i in range(5):
        print(i)
        
init=time.time()
print(init)        
usingfor()
t1=time.time() - init
init=time.time() - init
usingwhile()
print(time.time() - init )
print(t1)


print(4)
time.sleep(5)     #it is used to stop for given seconds
print("this will run after 5 seconds")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t ) #it will show the current time


print(formatted_time)