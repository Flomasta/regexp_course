import re

data = input()
pattern = r'(?:Категория: )(?:[А-Яа-яЁё ]+\\n)'
res = re.split(pattern, data)
print(res)
