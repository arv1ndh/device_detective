from make_dict import make_dict
from user_agents import parse
from pymongo import MongoClient


def lambda_handler(event, context):
    f = open("mongo_url.txt", "r")
    url = f.read()
    f.close()
    mon_client = MongoClient(url)
    db = mon_client.user_agents
    posts = db.posts
    
    ua = event["Records"][0]["body"]
    parsed_ua = parse(ua)
    parsed_dict = make_dict(parsed_ua)
    posts.insert_one(parsed_dict)
