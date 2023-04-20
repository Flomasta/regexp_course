import re

pattern = r'(am|pm)'
data = 'It\'s already 12:00am and I still don\'t want to sleep.'
res = re.sub(pattern, lambda x: 'pm' if x[0] == 'am' else 'am', data)
print(res)
