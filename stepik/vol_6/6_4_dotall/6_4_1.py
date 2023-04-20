import re

text = ''''spamstartЭТОТ
ТЕКСТ
НАХОДИТСЯ
НА
НЕСКОЛЬКИХ
СТРОКАХ
endspam
'''
pattern = r'^.*(?:start)(.*)(?:end)'
print(re.findall(pattern, text, flags=re.DOTALL))
