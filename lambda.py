def double(x):
    return x*2
d=double(5)
print(d)
double1=lambda x:x*2
cube=lambda x:x**3
print(cube(5))
print(double1(5))

avg=lambda x,y,z:(x+y+z)/2
print(avg(4,5,4))

def apply(fun,value):
    return 6+fun(value)

print(apply(lambda x:x*x,4))