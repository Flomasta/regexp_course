import re

data = input()
pattern = r'\w+'
res = re.finditer(pattern, data)
if res:
    [print(i.group()) for i in res]
