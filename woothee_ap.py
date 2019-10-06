#first do pip install woothee

import woothee
print(woothee.parse("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"))
# => {'name': 'Internet Explorer', 'category': 'pc', 'os': 'Windows 7', 'version': '8.0', 'vendor': 'Microsoft', 'os_version': 'NT 6.1'}
