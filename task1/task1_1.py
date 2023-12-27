import re

def is_valid_url(url):
    pattern = re.compile(r'(.*?)(/*minio/*admin/*v3/*update\?updateURL=)(http|https)?:\/\/(\S+)')

    return bool(pattern.match(url))


urls = [
    'test.com/minio/admin/v3/update?updateURL=https://example.com',
    'test.com/minio/admin///v3/update?updateURL=http://example.com',
    'test.com//minio//admin///v3/update?updateURL=/etc/passwd',
    'test.com/minio/admin/v3//update?updateURL=..//etc///passwd',
]

for url in urls:
    print(f'{url} - {is_valid_url(url)}')