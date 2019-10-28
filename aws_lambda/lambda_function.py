from make_dict import make_dict
from user_agents import parse
from pymongo import MongoClient
import time
import boto3


def lambda_handler(event, context):
    dyn_client = boto3.client('dynamodb')
    body = event["Records"][0]["body"]
    f = open("dynDB_table.txt", "r")
    table = f.read()
    f.close()
    response = dyn_client.get_item(TableName=table, Key={'macua' : {'S' : body } } )
    try:
        match = response['Item']
    except:
        expire = int(time.time() + 3600*24*30)
        response = dyn_client.put_item(TableName=table, Item={ 'macua' : { 'S' : body }, 'ttl' : { 'N' : str(expire) } })
        mac, delim, ua = body.partition('ua')
        parsed_ua = parse(ua)
        parsed_dict = make_dict(parsed_ua, mac)
        f = open("mongo_url.txt", "r")
        mongo_url = f.read()
        f.close()
        mon_client = MongoClient(mongo_url)
        db = mon_client.user_agents
        posts = db.posts
        posts.insert_one(parsed_dict)
    