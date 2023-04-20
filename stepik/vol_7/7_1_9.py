import re


def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


pattern = r'(\b\w+\b)'
data = 'x xx xxx xxxx xxxxx xxxxxx xxxxxxx xxxxxxxx xxxxxxxxx xxxxxxxxxx xxxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxxx xxxxxxxxxxxxxx'
res = re.sub(pattern, lambda x: x[0] if x[0] != 'x' and isprime(len(x[0])) else '', data)

print(' '.join(res.split()))
