import boto3
import random
import string
import time

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-west-1.amazonaws.com/809875841865/ua_headers.fifo'

ua_strings = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36', \
'Mozilla/5.0 (Linux; Android 4.3; C5502 Build/10.4.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36', \
'Mozilla/5.0 (Linux; Android 6.0; 4Good Light A103 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', \
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 EtsyInc/5.22 rv:52200.62.0', \
'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9']

while True:
    ua = ua_strings[random.randint(0, len(ua_strings)-1)]
    ID = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(128)])

    sent_ua = sqs.send_message(QueueUrl=queue_url, MessageBody=ua, MessageGroupId=ID)
    print("User-agent string sent to AWS queue:\n", ua)
    time.sleep(1)