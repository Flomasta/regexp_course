import re

pattern = re.compile(r'(?:(?:[\dA-F]{2}:?){6})')
data = '108:4F:E9:83:32:7720E:DC:33:F0:73:B0399:AB:A0:67:10:4D468:2D:E0:3A:01:E95CC:68:92:A5:59:796A7:D7:34:9E:09:9F7'
res = pattern.findall(data)
print(res)
