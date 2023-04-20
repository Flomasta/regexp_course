import re

data = input()
pattern = r'([a-z]+\s){11}|(\1){17}|(\1){23}'
result = re.match(pattern, data)

if result:
    print('возможно, это seed-фраза')
