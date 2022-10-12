# pip install requests로 requests설치
# 경로: c:\users\knh30\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages

import requests
r = requests.get('https://github.com/kimnamhyeon0112')
print(r.status_code)