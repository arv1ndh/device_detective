from device_detector import DeviceDetector
import boto3
import pymongo
from pymongo import MongoClient
import hashlib
import time

sqs = boto3.client('sqs')
f = open("sqs_url.txt", "r")
queue_url = f.read()
f.close()

f = open("mongo_url.txt", "r")
mongo_url = f.read()
f.close()
mon_client = MongoClient(mongo_url)
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
            parsed_string = DeviceDetector(ua).parse()
            posts.insert_one(parsed_string.all_details)
            print("Parsed UA information sent to Mongo database.")
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    except:
        pass
