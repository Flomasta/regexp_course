import re

pattern = r'(?P<inch>(?<!\$)\b\d+(,\d+)?(\sдюйма|\"))|(?P<bucks>\$\d+,?\d+?\b)'
main_data = 'SCBRHMI Серийный ЖК-дисплей HMI TFT с сенсорной панелью 10,4 дюйма - $95,25'


def convert(num):
    return num.replace(',', '.')


def replacer(item):
    item = item[0]
    if ' ' in item:
        item = item.split()[0]
    else:
        item = item.replace('"', '')

    if item.startswith('$'):
        return str(round(float(convert(item).replace('$', '')) * 59.5, 2)).replace('.0', '').replace('.', ',') + ' руб'
    else:
        return str(round(float(convert(item)) * 2.54, 2)).replace('.0', '').replace('.', ',') + ' см'


res = re.finditer(pattern, main_data)
for i in res:
    main_data = re.sub(pattern, replacer, main_data)
print(main_data)
