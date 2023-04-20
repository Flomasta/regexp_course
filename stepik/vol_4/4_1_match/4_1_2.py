# Код писать сюда \(❤‿❤)/
import re

pattern = r'(?P<protocol>http[s]?)+:\/\/(?P<domain>[a-z.\d]*?)\/[a-z\/\d_-]*(?P<query>\?[^# ]*)?(?P<ancor>[#][a-z]*)?'

data = input()
res = re.finditer(pattern, data)

for i in res:
    print(f"Полная ссылка: {i[0]}")
    print(
        f"Протокол: {i.group('protocol')} | Домен: {i.group('domain')} | Параметры: {i.group('query') if i.group('query') else 'None'} | Якорь: {i.group('ancor') if i.group('ancor') else 'None'}",
        end='\n\n')
