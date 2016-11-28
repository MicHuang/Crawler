import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

WEBSITE_NAME = "concordia"
HOMEPAGE = "https://www.concordia.ca/"
DOMAIN_NAME = get_domain(HOMEPAGE)
QUEUE_FILE = WEBSITE_NAME + "/queue.txt"
CRAWLED_FILE = WEBSITE_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(WEBSITE_NAME, HOMEPAGE, DOMAIN_NAME)


# Creat job workers (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.deamon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue")
        create_jobs()


create_workers()
crawl()
