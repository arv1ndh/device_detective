from html.parser import HTMLParser
from urllib.request import urlopen, Request

CUSTOM_HEADER = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

useragent_warehouse = {}
UA_COLL = {"platforms": ["android", "blackberry", "chrome", "firefox", "linux", "playstation", "nokia", "windows", "ios", "macos"], "browsers": ["chrome", "firefox", "internet-explorer", "microsoft-edge", "opera", "safari", "uc-browser"]}
PARENT_CATEG_IDENTIFIER = "col-md-2 col-sm-3 col-xs-4 center-block category-block"

class UA_Scraper(HTMLParser):
    def __init__(self, interested_list = None):
        HTMLParser.__init__(self)
        self.entered_device_block = False
        self.interested_list = set(interested_list) if interested_list != None else None
        self.links = []
    
    def handle_starttag(self, tag, attrs):
        if 'li' == tag and ("class", PARENT_CATEG_IDENTIFIER) in attrs:
            self.entered_device_block = True
        if self.entered_device_block and 'a' == tag:
            link = dict(attrs)["href"]
            if self.interested_list and link.split('/')[-2] in self.interested_list:
                self.links.append(link)
            else:
                self.links.append(link)
            self.entered_device_block = False

def content_fetcher(url):
    url_object = urlopen(Request(url, headers=CUSTOM_HEADER))
    return str(url_object.read())

def main():
    ua_url = "https://www.handsetdetection.com/device-detection-database/"
    variety_list = ["browsers", "platforms"]
    categ_links = []
    ver_links = []

    for item in variety_list:
        parent_url = ua_url + item
        html_page = content_fetcher(parent_url)
        UAS_object = UA_Scraper(UA_COLL[item])
        UAS_object.feed(html_page)
        categ_links += UAS_object.links
    for link in categ_links:
        html_page = content_fetcher(link)
        Ver_object = UA_Scraper()
        Ver_object.feed(html_page)
        ver_links += Ver_object.links

if __name__ == "__main__":
    main()
