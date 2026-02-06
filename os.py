import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,12):
#     os.mkdir(f"data/day{i+1}")

# for i in range(0,12):
#    os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")

folder=os.listdir("data")    
print(folder)
 
for folder in folder:
     print(folder)
     
     print(os.listdir(f"data/{folder}"))
os.system     
print(os.getcwd())
# os.chdir("/C")
print(os.getcwd())