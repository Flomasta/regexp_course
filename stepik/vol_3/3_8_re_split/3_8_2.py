import re

data = input()
pattern = r'[.?!,\s]'
res = re.split(pattern, data)
print(res)
