import unittest

from states import http_check

def test_http_check_base():
    service = 'https://travis-ci.org/'
    word = http_check(service)
    assert isinstance(word, str)
