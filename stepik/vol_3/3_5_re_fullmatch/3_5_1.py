import re

res = re.fullmatch(r'\d{13,}', input())
print('True' if res else 'False')
