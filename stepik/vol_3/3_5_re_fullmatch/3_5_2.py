import re

data = input()
pattern = r'([a-zA-Z0-9@#$%^&*()_+!?-]){8,}$'
res = re.fullmatch(pattern, data)
print('True' if res else 'False')
