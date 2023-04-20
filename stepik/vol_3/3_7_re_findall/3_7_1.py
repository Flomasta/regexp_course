import re

data = input()
pattern = r'(https://imgur.com/[A-Za-z0-9]{7})'
res = re.findall(pattern, data)
if res:
    [print(i) for i in res]
