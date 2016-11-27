from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider():

    # class variables (shared among all instances)

    website_name = ""
    base_url = ""
    domain_name = ""
    queue_file = ""
    crawled_file = ""
    queue = set()
    crawled = set()

    def __init__(self, website_name, base_url, domain_name):
        Spider.website_name = website_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.website_name + "/queue.txt"
        Spider.crawled_file = Spider.website_name + "crawled.txt"
        self.boot()
        self.crawl_page("First Spider", Spider.base_url)

    @staticmethod
    def boot():
        create_website_dir(Spider.website_name)
        create_website_file(Spider.website_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled " + str(
                len(Spider.crawled)))
