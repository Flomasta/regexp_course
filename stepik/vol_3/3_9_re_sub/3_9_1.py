import re

pattern = r'[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]'
replace = '!'
data = input()
result = re.sub(pattern, replace, data)

print(result)
