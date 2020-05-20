import re

pattern=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string=input()
a= pattern.search(string)
if  a:
   print(a)
else:
   print("enter a valid email address")