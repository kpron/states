from requests import request

SERVICES = [
    'https://google.com',
    'https://ya.ru',
    'https://travis-ci.org',
    'https://telegram.org',
    'http://mocks.lol'
]


def http_check(url):
    req = request('GET', url)
    if req.status_code == 200:
        status = 'OK'
    else:
        status = 'FAIL'
    return "%s (%s)" % (status, req.elapsed.total_seconds())

