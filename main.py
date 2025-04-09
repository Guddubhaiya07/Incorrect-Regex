import re
num=int(input())
for _ in range(num):
   string=input()
   try:
    re.compile(string)
    print(True)
   except re.error:
    print(False)
