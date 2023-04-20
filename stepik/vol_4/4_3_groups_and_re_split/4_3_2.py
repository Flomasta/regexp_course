import re

pattern = r'([&?])'
data = 'https://stackoverflow.com/questions/tagged/regex?tab=votes&page=11&pagesize=15'

print(re.split(pattern, data))
