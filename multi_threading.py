import threading
import time
from concurrent.futures import ThreadPoolExecutor
#indicates some task being done

def fun(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds 
    
time1=time.perf_counter()
# fun(4)    
# fun(5)    
# fun(6)

t1=threading.Thread(target=fun,args=[4])    
t2=threading.Thread(target=fun,args=[2])    
t3=threading.Thread(target=fun,args=[1])  

t1.start()
t2.start()
t3.start()  

t1.join() #it used wait first till not complete
t2.join()
t3.join()
time2=time.perf_counter()
print(time2-time1)    

#concurrent.futures
def poolDemo():
    with ThreadPoolExecutor() as executor:
        # future=executor.submit(fun,3)
        # print(future.result())
        
        # future=executor.submit(fun,5)
        # print(future.result())
        
        # future=executor.submit(fun,4)
        # print(future.result())
        
        l=[3,5,1,2]
        results=executor.map(fun,l)
        for result in results:
            print(result)
            
poolDemo()        
    