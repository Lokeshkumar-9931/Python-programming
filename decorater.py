def greet(fx):
   def mfx(*args,**kwargs):
    print("good morning")
    fx(*args,**kwargs)
    print("thanks for using the function") 
   return mfx 

@greet
def hello():
    print("hello world")

@greet    
def add(a,b):
    add=a+b
    print(add)
    return add   

hello()
add(6,7)   