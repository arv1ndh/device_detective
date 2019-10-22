import boto3
from mitmproxy import http

sqs = boto3.client(service_name = 'sqs',region_name = "us-west-1", aws_access_key_id = "AKIAJPNXAACALE34XPPA", aws_secret_access_key="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")
QUEUE_URL = 'https://sqs.us-west-1.amazonaws.com/809875841865/ua_headers'

def request(flow: http.HTTPFlow):
    header_fields = flow.request.headers.fields
    for key,value in header_fields:
        if key == bytes("User-Agent",'utf-8'):
            ua_string = str(value, 'utf-8')
            sent_ua = sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=ua_string)
