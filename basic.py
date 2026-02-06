print("hello world")
print(5)
print("bye")
print(34*32)
print("hey i am a \"good boy \n and this viewer is\" also good boy")
'''
herry is good youtuber
'''
a=5
i=1
while i<=10:
    print(a*i)
    i+=1
m=a*i
print(m)
print("good",7,9.9,sep="~",end="\n009\n") #sep is used to seperate the values
print("lokesh")
print('\n')
print(2**3**2)
#output 512
numbers=[1,2,3,4]
numbers[1:3]=[8,9]
print(numbers)
#output
#[1,8,9,4]

def wiered_num(x=[]):
    x.append(1)
    return x
print(wiered_num())
print(wiered_num())
print(wiered_num())
print(wiered_num())
print(wiered_num())
#output
# [1]
# [1, 1]
# [1, 1, 1]
# [1, 1, 1, 1]
# [1, 1, 1, 1, 1]

a=[1,2,3]
print(a[3:]) #output null
a=[1,2,3]
b=a
b.append(4)
print(a)
#output [1, 2, 3, 4]
x=bool(0)
print(x)
#flase
print([x for x in range(10) if x % 2 == 0])
l=['a','b','c','d','e']
l[1:4]=['x','Y']
print(l)

a='python'
if a=='java' or 'html':
    print("accessed")
else:
    print("not accessed")


b=True
if b==1:
    print('yes')
else:
    print('no')

lst=[34,43,54,65,76]
lst[2]=[56,87]
print(lst)   


lst=[]
i=0
while i<=5:
    lst.append(int(input("enter a value: ")))
    i+=1 
print(lst)    

    