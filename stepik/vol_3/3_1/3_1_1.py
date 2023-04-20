import re

pattern = r'П.+?т'
text = 'Привет, как тебя зовут?'
match = re.match(pattern, text)

print(match)

# span - индексы начала и конца совпадения, а match - само совпадение.
# <re.Match object; span=(0, 6), match='Привет'>

print(match.group())
