import re

data = 'Ловите дату, разделённую точками: 01.22.2089.'

pattern = r'(\d+)(/|\.)(\d+)(\2)(\d+)'
res = re.sub(pattern, r'\3\2\1\4\5', data)
print(res)
