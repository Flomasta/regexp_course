import re

data = input()
pattern = r'[0-2][0-9]:[0-5][0-9]'
res = re.findall(pattern, data)
if res:
    [print(i[0]) for i in res]
