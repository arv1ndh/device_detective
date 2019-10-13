from ua_parser import user_agent_parser
import boto3
import pymongo
from pymongo import MongoClient
import hashlib

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-west-1.amazonaws.com/809875841865/ua_headers.fifo'

mon_client = MongoClient("mongodb+srv://chadbloxham:Lakers24gokobe@cluster0-kdfv3.mongodb.net/test?retryWrites=true&w=majority")
db = mon_client.user_agents
posts = db.posts

hash_db = []

while True:
    try:
        response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
        receipt_handle = response["Messages"][0]["ReceiptHandle"]
        ua = response["Messages"][0]["Body"]
        h = hashlib.sha256(ua.encode())
        if h.hexdigest() not in hash_db:
            hash_db.append(h.hexdigest())
            print("User-agent string received from AWS queue:\n", ua)
            parsed_string = user_agent_parser.Parse(ua)
            posts.insert_one(parsed_string)
            print("Parsed UA information sent to Mongo database.")
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    except:
        pass
