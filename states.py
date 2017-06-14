from requests import request

SERVICES = [
    'https://travis-ci.org',
    'https://github.com/',
    'https://hub.docker.com',
    'https://google.com',
    'https://ya.ru',
    'https://telegram.org'
]


def http_check(url):
    req = request('GET', url)
    if req.status_code == 200:
        status = 'OK'
    else:
        status = 'FAIL'
    return "%s (%s)" % (status, req.elapsed.total_seconds())

