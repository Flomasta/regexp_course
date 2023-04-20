import re

pattern = r'П.+?т'
text = 'Привет, как тебя зовут?'
match = re.match(pattern, text)

# Код писать сюда \(❤‿❤)/
print(match.group())
print(match.start(0))
print(match.end(0))
print(match.pos)
print(match.endpos)
print(match.re)
print(match.string)
