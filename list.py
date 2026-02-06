list=[454,7,768,76,8787,"lokesh","ravi",4,765,3456,98765,23456789,123456789]
print(list)
print(len(list))
print(list[0],list[1],list[2])
list.append(56)
print(list)
print(list.pop(0))
print(list[-3])
if 7 in list:
    print("yes")
else:
    print("no")    
if "lok" in "lokesh":
    print("yes")    
else :
    print("no")    
print(list[:7:2])    #[0:3:2(jump)]

#list comprehsion
lst=[i*i for i in range(18)] #square of the numbers
print(lst)
lst=[i*i for i in range(18) if(i%2==0)] #square of the even numbers
print(lst)

#list method
lst.append(324)
lst.sort()
lst.sort(reverse=True)
lst.remove(lst[9])
print(lst)
print(lst.index(4))
print(lst.count(1))
m=lst.copy
print(m)
lst.insert(2,56)
print(lst)
k=[6,7,4,89,"lokesh"]
#m.extend(k)
print(k)
l=lst+k
print(l)


