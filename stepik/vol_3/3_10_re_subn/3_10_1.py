import re

pattern = r'[.?!,:]'
replace = ''
data = input()
result, amount = re.subn(pattern, replace, data)

print(amount)
