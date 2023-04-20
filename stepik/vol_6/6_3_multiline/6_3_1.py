import re, sys

text = '''$$^^$^$$4^^$^^$$$
^$^$
^$$^$^^^$^^$$^$$$$
^^^^$$S^$^$^$^$^^$$'''
# Код писать сюда \(❤‿❤)/

pattern = r'^(?:\^|\$)+$'
match = re.findall(pattern, text, flags=re.MULTILINE)
if match:
    print(match)
