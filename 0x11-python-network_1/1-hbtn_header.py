#!/usr/bin/python3
""" Takes in URL, send a request to the URL """

from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as pg:
        print(pg.getheader("X-Request-Id"))
