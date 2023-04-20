import re

pattern = r'\d+'
data = '2 в квадрате это 4'
res = re.sub(pattern, lambda m: str(int(m.group()) ** 2), data)
print(res)
