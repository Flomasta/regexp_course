import re

data = input()
pattern = r'\b\w{5}\b'
res = re.finditer(pattern, data)
if res:
    [print(i.group()) for i in res]
