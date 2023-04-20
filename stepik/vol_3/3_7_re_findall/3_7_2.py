import re

data = input()
pattern = r'([A-Za-z0-9_\-]+@[a-zA-Z0-9]+.(com|ru))'
res = re.findall(pattern, data)
if res:
    [print(i[0]) for i in res]
