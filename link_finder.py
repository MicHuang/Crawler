import HTMLParser
import urllib


class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print tag

    def error(self, message):
        pass


finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head></html>')