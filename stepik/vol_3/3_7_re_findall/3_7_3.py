import re

data = input()
pattern = r'((\d{2}\.\d{2}\.\d{4})|(\d{4}\.\d{2}\.\d{2})|(\d{2}\/\d{2}\/\d{4})|(\d{4}\/\d{2}\/\d{2}))'
res = re.findall(pattern, data)
if res:
    [print(i[0]) for i in res]
