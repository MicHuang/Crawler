import os


# Each website need a separate directory..
def create_website_dir(directory):
    if not os.path.exists(directory):
        print "Creating folder " + directory
        os.makedirs(directory)
    else:
        print "The folder " + directory + " exists."


# In the website dir, we need queue file and crawled file
def create_website_file(website, base_url):
    queue = website + "/queue.txt"  # waiting for crawling
    crawled = website + "/crawled.txt"  # the URLs it crawled
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# add data on to the existing file
def append_file(path, data):
    with open(path, "a") as f:
        f.write(data + "\n")
        f.close()


# delete the file
def delete_file_contents(path):
    with open(path, "w"):
        pass


# Read a file and convert each line into a set
def file_to_set(file):
    results = set()
    with open(file, "rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results


#iterate through a set, each set item will be a line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_file(file, link)
