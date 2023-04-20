import re

data = 'Ихние книги лежали на полке.'
pattern = r'(([Ее]го|[Ее]ё|[Ии]х)[а-я]+)'
res = re.sub(pattern, r'\2', data)
print(res)
