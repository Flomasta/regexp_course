import re

data = input()
pattern = r'\b\d+,\d* ₽'
res = re.finditer(pattern, data)
if res:
    [print(i.group()) for i in res]
