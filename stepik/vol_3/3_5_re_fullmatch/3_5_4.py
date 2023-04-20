import re

data = input()
pattern = r'[+-]?\d*(?:x\^\d+|x)?\b)+'
res = re.fullmatch(pattern, data)
print('True' if res else 'False')
