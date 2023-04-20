import re

lastname, name, surname = input().split()
str_data = input()
replace = 'ФИО'
pattern = fr'{lastname}[а-я]* ({name[0]}\.|{name[:-1]}[а-я]*) ({surname[0]}\.|{surname[:-1]}[а-я]*)'
result = re.sub(pattern, replace, str_data)
print(result)
