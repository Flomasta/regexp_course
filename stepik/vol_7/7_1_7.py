import re

pattern = r'(?<!0)(?:(0|[1-9][0-9]?|(1[0-9]?[0-9]|2[0-5]?[0-5]))(\.|$)){4}'
data = input()
res = re.match(pattern, data)

print(('True', res.group()) if res else 'False')
