import re

pattern = r'(([A-Z][a-z]+?)|([0-9]+))'
data = 'SomeNumbers123'
result = re.sub(pattern, lambda x: f'_{x[0]}', data)

print(result.strip('_').lower())
