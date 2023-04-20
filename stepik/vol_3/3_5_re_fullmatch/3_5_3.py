import re

data = input()
pattern = r'\+?\d+[ ]?(\()?\d{3}(?(1)\)|)[ ]?\d{3}(?: |-)?\d{2}(?: |-)?\d{2}'
res = re.fullmatch(pattern, data)
print('True' if res else 'False')
