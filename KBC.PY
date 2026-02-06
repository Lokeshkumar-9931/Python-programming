questions=[
    ["which language was  used to create fb? ","python",
    "french","Javascript","php",4],
    ["which language was  used to create what's app? ","python",
    "french","Javascript","php",3],
    ["which language was  used to create instagram? ","python",
    "jango","Javascript","php",2],
    ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],
     ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],
      ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],
       ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],
        ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],
         ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],
          ["which language was  used to create railyatri? ","python",
    "c","Javascript","c++",2],   
]
levels=[1000,2000,3000,5000,10000,20000,40000,
        80000,160000,320000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question for Rs. {levels[i]}\n")
    print(f"the question is {questions[i][0]}")
    print(f"a. {questions[i][1]}  b.{questions[i][2]} ")
    print(f"c. {questions[i][3]}  d.{questions[i][4]} ")
   
    reply=int(input("enter your anwer (1-4) "))
    if(reply==question[-1]):
        print(f"correct answer,you have won Rs.{levels[i]}")
        if(i==4):
            money=1000
        elif(i==9):
            money=320000
        elif(i==14):
            money =70000000      
    else:
        print("wrong answer!")    
        break

print(f"your take home money is {money}")    