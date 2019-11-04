import json
import time
import random
from urllib.request import urlopen,Request

with open("user_agents.json", 'r') as ua_file:
    UA_DATA = json.loads(ua_file.read())

WEB_LIST = [ "http://google.com", "http://facebook.com", "http://reddit.com"] 

def random_macro(sequence):
    if type(sequence) == dict:
        return random.choice(list(sequence.keys()))
    return random.choice(list(sequence))

class Ua_Simulator:
    def __init__(self, users, time):
        self.pcategory = random_macro(["platforms", "browsers"])
        self.category = random_macro(UA_DATA[self.pcategory])
        self.version = random_macro(UA_DATA[self.pcategory][self.category])
        self.ua = set()
        self.n_users = users
        self.simul_time = time

    def unique_ua_generator(self):
        i = 0
        while i < self.n_users:
            ua = random_macro(UA_DATA[self.pcategory][self.category][self.version])
            if ua not in self.ua:
                self.ua.add(ua)
                i += 1

    def requests_sender(self):
        end_time = time.time() + 60 * self.simul_time
        while time.time() < end_time:
            web_site = random_macro(WEB_LIST)
            ua = random_macro(self.ua)
            url_obj = urlopen(Request(web_site, headers={"User-Agent": ua}))

def main():
    user_count = int(input("Enter no of users: "))
    access_time = int(input("Enter total time to simulate: "))
    ua_simul_obj = Ua_Simulator(user_count, access_time)
    ua_simul_obj.unique_ua_generator()
    ua_simul_obj.requests_sender()
        

if __name__ == "__main__":
    main()
