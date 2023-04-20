import re


def get_x(m):
    return {'o': 'x', 'O': 'X'}[m[0]]


print(re.subn('O', get_x, input(), flags=re.IGNORECASE)[0])
