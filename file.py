f=open("myfile.txt","r")
# f.write("my name is krishna vashudev yadav \n")
data=f.read()
print(data)
f.close()

f=open("myfile.txt","a")
# f.write("krishna is the lord of lords  \n")
print(f.read)
f.close()

#with
with open ("myfile.txt",'a+') as r:
    r.write("\n Radhey Radhey ")
    data=r.read()
    print(data)  

#methds of file handling
f=open("myfile.txt","r")
while True:
    line=f.readline() 
    print(line,type(line))   
    if not line:
        break
    print(line)
f=open('marks.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not (line):
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    m4=int(line.split(",")[3])
    print(f"Marks of students {i} in Maths is: {m1}")
    print(f" Marks of students {i} in english is: {m2}")
    print(f"Marks of students {i} in science is: {m3}")
    print(f"Marks of students {i} in science is: {m4}")
    
    print((line))