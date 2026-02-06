with open ('file.txt ','r')as r:
    print(type(r))
#move to the 10th bytes in the file
    r.seek(10)    
#read the next 5bytes
    print(r.tell())  # it tell us about the position of text font
    data=r.read(5)
    print(data)

with open('file.txt','w') as t:
    t.write("hello lokesh")
    t.truncate(5) # it allow only given number text to print in file
with open('file.txt','r') as t:
    print(t.read())
            