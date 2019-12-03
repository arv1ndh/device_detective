#env http_proxy=http://localhost:8080 python user_simulator.py

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
    def __init__(self, users, reqs, simul_type, additional_type):
        self.pcategory = random_macro(["platforms", "browsers"]) if simul_type == "random" else simul_type
        self.category = random_macro(UA_DATA[self.pcategory]) if additional_type == "random" else additional_type
        self.version = random_macro(UA_DATA[self.pcategory][self.category])
        self.ua = set()
        self.n_users = users
        self.req_count = reqs
        if additional_type == "random":
            self.r_flag = True
        else:
            self.r_flag = False

    def __repr__(self):
        return {"pcategory": self.pcategory, "category": self.category, "version": self.version, "ua": self.ua}

    def unique_ua_generator(self):
        i = 0
        while i < self.n_users:
            if self.r_flag:
                self.category = random_macro(UA_DATA[self.pcategory])
                self.version = random_macro(UA_DATA[self.pcategory][self.category])

            ua = random_macro(UA_DATA[self.pcategory][self.category][self.version])
            if ua not in self.ua:
                self.ua.add(ua)
                i += 1
        self.ua = list(self.ua)

    def requests_sender(self):
        n_req = 0
        while n_req < self.req_count:
            web_site = "http://reddit.com"#random_macro(WEB_LIST)
            emp_id = random.randint(1,len(self.ua)) - 1
            ua = self.ua[emp_id]
            emp_info = f"Employee_{emp_id}"
            print(ua, emp_info)
            url_obj = urlopen(Request(web_site, headers={"User-Agent": ua, "Employee": emp_info}))
            n_req += 1

def main():
    user_count = int(input("Enter no of users: "))
    req_count = int(input("Enter total no of hits to simulate: "))
    simul_type = input(f"What kind of simulation do you want? [{', '.join(list(UA_DATA.keys())) + ', random'}] \nEnter choice:  ")
    if simul_type != "random":
        additional_type = input(f"What kind of {simul_type} do you want? [{', '.join(list(UA_DATA[simul_type].keys())) + ', random'}] \nEnter choice: ")
    else:
        additional_type = "random"
    ua_simul_obj = Ua_Simulator(user_count, req_count, simul_type, additional_type)
    ua_simul_obj.unique_ua_generator()
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(ua_simul_obj.__repr__())
    #return
    ua_simul_obj.requests_sender()
        

if __name__ == "__main__":
    main()
