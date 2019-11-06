import boto3
import json
from mitmproxy import http

with open("conf.json") as json_f:
    data = json.load(json_f)

sqs = boto3.client(service_name = data["service_name"],region_name = data["region_name"], aws_access_key_id = data["key_id"], aws_secret_access_key = data["access"])

def request(flow: http.HTTPFlow):
    header_fields = flow.request.headers.fields
    for key,value in header_fields:
        if key == bytes("User-Agent",'utf-8'):
            ua_string = str(value, 'utf-8')
        if key == bytes("Employee", 'utf-8'):
            emp_string = str(value, 'utf-8')
    fin_string = f"{emp_string}ua{ua_string}"
    sent_ua = sqs.send_message(QueueUrl=data["q_url"], MessageBody=fin_string)
