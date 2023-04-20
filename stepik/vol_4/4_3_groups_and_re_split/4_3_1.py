import re

pattern = r'[a-zA-Zа-яА-ЯёЁ.,]+'
data = '3снова+в5 *тексте6спам-.4 : 4 = 32'
res = re.split(pattern, data)

print(res)
