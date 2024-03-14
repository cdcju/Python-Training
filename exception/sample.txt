import re

email = """ 
abcd@gmail.com
efgh@yahoo.co.in
agnichakra.1984@gmail.com
"""

pattern = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+')

matches = pattern.finditer(email)

for i in matches:
    print(i)