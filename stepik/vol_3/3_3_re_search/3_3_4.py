import re

data = 0
pattern = r'(?:t=)(\d+\.\d+\+\d+)'
while not data:
    data = re.search(pattern, input())
    print(data.group())
