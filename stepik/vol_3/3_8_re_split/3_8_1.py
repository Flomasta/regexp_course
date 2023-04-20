import re

data = input()
pattern = r'[.?!]'
res = re.split(pattern, data)
print(res)
