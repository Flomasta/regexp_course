import re
import sys

data = list(map(str.strip, sys.stdin.readlines()))
pattern = r'[Кк]од'
lst = []
for n, i in enumerate(data,1):
    res = re.search(pattern, i)
    if res:
        lst.append(res)
        print(n, res.start())
if len(lst) == 0:
    print('код не найден')
