#MAP
def cube(x):
    return x**3
print(cube(5))

l=[1,2,3,4,5,6,7]
newl=list(map(cube,l)) #map is use to use the functions in single line
New1=list(map(lambda x:x**3,l))
print(New1)
print(newl)

#FILTER
def filter_function(a):
    return a>4

new_l=list(filter(filter_function,l))
new_L=list(filter(lambda a:a>4,l))
print(new_l)
print(new_L)
print("\n")

#REDUCE
from functools import reduce
#list of numbers
numbers=[1,2,4,6,7,8]

#calculate the sum of the numbers
def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)
print(sum)
