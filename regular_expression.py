import re


pattern="[a-z]+haiya"
text='''
bhaiya me bhaiya munna bhaiya
bhaiy mukh bihar ,bhaiy mukh bihar'''
'''bhaiya me bhaiya munna bhaiya
bhaiy mukh bihar ,bhaiy mukh bihar'''
'''bhaiya me bhaiya munna bhaiya
bhaiy mukh bihar ,bhaiy mukh bihar'''

# match=re.search(pattern,text)
# print(match)
matches=re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])

