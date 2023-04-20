import re

data = input()
start_pos = int(input())
end_pos = int(input())

pattern = re.compile(r'(?<![a-z])([a-z]+)')
match = pattern.search(data, pos=start_pos, endpos=end_pos)
if match:
    print(match[0])
