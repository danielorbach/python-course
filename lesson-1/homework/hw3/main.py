"""
Homework 2: Log Puzzle
Link: developers.google.com/edu/python/exercises/log-puzzle

An image of an animal has been broken it into many narrow vertical stripe images.
The stripe images are on the internet somewhere, each with its own url.
The urls are hidden in a web server log file.
Your mission is to find the urls and download all image stripes to re-create the original image.
"""

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

import os
import re
import sys
from urllib import request


def create_puzzle_path(line):
    # two re options to try:
    # 1) r'(?<=GET )\S+' and grab full match
    # 2) r'GET (?P<path>\S+) HTTP' and grab path group match
    match = re.search(r'(?<=GET )\S+', line)
    if match:
        path = match.group(0)
        if 'puzzle' in path:
            return path
    return ''


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    http_prefix = 'http://'
    server_name = filename.split('_', maxsplit=1)[1]
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath) as file:
        all_lines = file.readlines()
    valid_urls = []
    for line in all_lines:
        puzzle_path = create_puzzle_path(line)
        if puzzle_path:
            full_url = http_prefix + server_name + puzzle_path
            valid_urls.append(full_url)
    # remove duplicates and sort the valid urls by increasing order
    valid_urls = list(set(valid_urls))
    valid_urls.sort()
    return valid_urls


def int_sort(val):
    return int(val[3:])


def create_index(dir_path):
    """
    example index.html
    <html>
    <body>
    <img src="/edu/python/exercises/img0"><img src="/edu/python/exercises/img1"><img src="/edu/python/exercises/img2">...
    </body>
    </html>
    """
    all_files = os.listdir(dir_path)
    img_files = [file for file in all_files if 'img' in file]
    img_files.sort(key=int_sort)
    index_path = os.path.join(dir_path, 'index.html')
    index_prefix = """<html>
    <body>
    """
    index_img_start = '<img src="'
    index_img_end = '">'
    index_suffix = """
    </body>
    </html>"""
    with open(index_path, 'w') as index_file:
        index_file.write(index_prefix)
        for img in img_files:
            img_path = os.path.join(dir_path, img)
            index_file.write(index_img_start + img_path + index_img_end)
        index_file.write(index_suffix)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    dir_path = os.path.join(os.getcwd(), dest_dir)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    print('starting to download images', end='\n\n')
    i = 0
    for url in img_urls:
        img_name = f'img{i}'
        img_path = os.path.join(dir_path, img_name)
        print(f'downloading image: {img_name}')
        request.urlretrieve(url, img_path)
        print(f'{img_name} download complete', end='\n\n')
        i += 1
    print('all images downloaded. creating index.html')
    create_index(dir_path)
    print('index.html created')


def main():
    args = sys.argv[1:]

    if not args:
        print
        'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
