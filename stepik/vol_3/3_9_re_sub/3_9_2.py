import re

pattern = r'[<.*?>]'
replace = ''
data = input()
result = re.sub(pattern, replace, data)

print(result)
