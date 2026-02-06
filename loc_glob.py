x=4 #global
print(x)

def hello():
    global x
    x=23
    y=35
    print("hello lokesh")
    print(y)#local
    print(x)

hello()    
