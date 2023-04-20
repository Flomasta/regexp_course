import re

data = input()
pattern = r'[A-Za-z]+'
result = re.match(pattern, data)
if result:
    print('Первое слово в предложении:', result.group())
