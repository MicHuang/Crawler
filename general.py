import os


# Each website need a separate directory..
def create_website_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print('The file ' + directory + " exist.")


# In the website dir, we need queue file and crawled file
def create_website_file(website, base_url):
    queue = website + "/queue.txt"
    crawled = website + "/crawled.txt"
    if not os.path.isfile("queue"):
        write_file(queue, base_url)
    if not os.path.isfile("crawled"):
        write_file(crawled, "")


def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# add data on to the existing file
def append_file(path, data):
    with open(path, mode="a") as f:
        f.write("\n" + data)


# delete the file
def delete_file_contents(path):
    with open(path, mode="w") as f:
        pass


# Read a file and convert each line into a set
def file_to_set(file):
    results = set()
    with open(file, mode="rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results


#iterate through a set, each set item will be a line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_file(file, link)
