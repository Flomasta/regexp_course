import re
import sys

data = lines = list(map(str.strip, sys.stdin.readlines()))
pattern = r'(?<=Activation key: )((?:[A-Z0-9]){5}\-){4}([A-Z0-9]){5}'
for i in data:
    res = re.search(pattern, i)
    if res:
        print(res.group())
