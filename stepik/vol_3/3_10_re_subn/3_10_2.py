import re

pattern = r'[0-9]'
replace = 'X'
data = input()
result = re.subn(pattern, replace, data)

print(result)
