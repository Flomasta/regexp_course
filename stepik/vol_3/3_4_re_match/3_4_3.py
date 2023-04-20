import re

data = input()
pattern = r'.*(?=@)'
result = re.match(pattern, data)
if result:
    print(result.group())
