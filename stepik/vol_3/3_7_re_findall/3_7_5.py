import re

data = input()
pattern = r'(\<a)(.*?)(href=\")(.*?)(\")(.*?)(\>)'
res = re.findall(pattern, data)
for i in res:
    print(i[3])
