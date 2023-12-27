import re

def is_valid_filename(filename):
    pattern = re.compile(r'^\s*[\w\d\s@#$%^&*()_+-=,.;\'{}[\]]+\.(jpg|jpeg|png|gif)\s*$')

    return bool(pattern.match(filename))


files = [
    'SecSignal.jpg',
    'test.exe',
    '123.jpg',
    ' filename_with space at_the_beginning_and_at_the_end.jpg ',
    '123@asdklj123@#$%^&*@2_asd**@[].jpg',
    'SecSignal.jpg;echo 3c3f7068702073797374656d28245f4745545b2263225d293b203f3e0a | xxd -r -p > SecSignal.php;echo SecSignal.jpg',
]

for file in files:
    print(f'{file} - {is_valid_filename(file)}')