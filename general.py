import os


# Each website need a separate directory..
def create_website_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print('The file ' + directory + " exist.")


# In the website dir, we need queue file and crawled file
"""
def create_website_file(website, base_url):


def write_file(path, data):


# add data on to the existing file
def append_file(path, data):


# delete the file
def delete_file_contents(path):


# Read a file and convert each line into a set
def file_to_set(file):


#iterate through a set, each set item will be a line in the file
def set_to_file(links, file):

"""
