from requests import request

SERVICES = [
    'https://google.com',
    'https://ya.ru',
    'https://travis-ci.org'
]


def http_check(url):
    req = request('GET', url)
    return "%s - %s" % (req.status_code, req.elapsed.total_seconds())

