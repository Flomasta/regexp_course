import re

pattern = r'(:?<p.*?>)(.*?)(:?<\/p>)'
data = input()
res = re.findall(pattern, data)
if res:
    for i in res:
        if i[1]:
            print(i[1])
