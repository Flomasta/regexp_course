import re

data = input()
res = re.sub(r'.{1,5}$', re.match(r'^.{1,5}', data).group(), data)
print(res)
