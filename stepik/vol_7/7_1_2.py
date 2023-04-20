import re

pattern = r'_'
data = 'my_send_message'
res = re.split(pattern, data)
print(''.join(list(map(lambda x: x.capitalize(), res))))
