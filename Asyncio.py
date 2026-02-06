import time
import asyncio
async def function1():
    await asyncio.sleep(1)
    print("fun 1")
    return "lokesh"

async def function2():
    await asyncio.sleep(1)
    print("fun 2")

async def function3():
    await asyncio.sleep(1)
    print("fun 3")

async def function4():
    await asyncio.sleep(1)
    print("fun 4")
async def main():
     await function1()    
     await function2()    
     await function3()    
     await function4()
    
#  L = await asyncio.gather(  
#         function1(),    
#         function2(),    
#         function3(),    
#         function4(),
#    )  

 #print(L)  
 
asyncio.run(main())  