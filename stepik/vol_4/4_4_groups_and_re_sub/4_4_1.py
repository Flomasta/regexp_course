import re

data = 'Тут два два слова подряд!'
re.sub(r'([а-яА-яЁё]+?\s?)(\1)', r'\1', data)

print(data)
