import re

txt = "AI is the rain"
x= re.findall("bangladesh" , txt)
print(x)

# 

str = "this is India: A country in south\'s Aisa"

result = re.split(r'\W+',str)
print(result)

#replace
str = "this is India: A country in south\'s Aisa"

result = re.sub(r'India', "Bangladesh" , str)
print(result)
