import re


def find_repeated(data):
    pattern = r'(\b\w+\b)(.*?)\s(\1)'
    res = re.search(pattern, data)
    return res.group(1) if res else 'None'

find_repeated('ap fl hk ap hk fl')
find_repeated('yes no eyes no maybe')
