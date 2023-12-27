import re

def is_valid_community(str):
    pattern = re.compile(r'^[\w\s\-]+$')

    return bool(pattern.match(str))


test_strings = [
    'test etst tdasd',
    'флыовдл',
    'asdas 123 asdad',
    '123_asd_zxczxc',
    "asd'; echo 1",
    "test.exe",
    "'",    
]

for t_str in test_strings:
    print(f'{t_str} - {is_valid_community(t_str)}')