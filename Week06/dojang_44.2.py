import urllib.request

response = urllib.request.urlopen('https://github.com/kimnamhyeon0112')
print(response.status)
print()

import urllib.request as r
response = r.urlopen('https://github.com/kimnamhyeon0112')
print(response.status)
print()

from urllib.request import Request, urlopen
req = Request('https://github.com/kimnamhyeon0112')
response = urlopen(req)
print(response.status)
print()

from urllib.request import *
req = Request('https://github.com/kimnamhyeon0112')
response = urlopen(req)
print(response.status)
print()

from urllib.request import Request as r, urlopen as u
req = r('https://github.com/kimnamhyeon0112')
response = u(req)
print(response.status)