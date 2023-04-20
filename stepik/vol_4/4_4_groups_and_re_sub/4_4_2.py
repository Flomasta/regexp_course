import re

pattern_1 = r'(\*{2})(.*?)(\1)'
pattern_2 = r'(\*{1})(.*?)(\1)'
data = 'А тут и **Bold text**, и *Italic*!'

res = re.sub(pattern_1, r'<strong>\2</strong>', data)
result = re.sub(pattern_2, r'<em>\2</em>', res)
print(result)
