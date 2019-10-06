#first do pip install httpagentparser

import httpagentparser
s = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) \
        Chrome/5.0.307.11 Safari/532.9"
#print(httpagentparser.simple_detect(s))
#print(httpagentparser.detect(s))

s = "Mozilla/5.0 (Linux; U; Android 2.3.5; en-in; HTC_DesireS_S510e Build/GRJ90) \
        AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
#print(httpagentparser.simple_detect(s))
print(httpagentparser.detect(s))
