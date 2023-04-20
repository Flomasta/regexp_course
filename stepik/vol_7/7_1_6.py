import re

consonants = r'[bcdfghjklmnpqrstvwxyz]'
vovels = r'[aeiouy]'

pattern = fr'(?i)\b(?:{vovels}{consonants})+{vovels}?\b|\b(?:{consonants}{vovels})+{consonants}?\b'
data = input()
res = re.findall(pattern, data)
print(*res)
