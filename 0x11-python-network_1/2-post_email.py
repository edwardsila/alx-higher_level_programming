#!/usr/bin/python3
""" THis script  takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8) """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    data = parse.urlencode({'email': email}).encode()

    with request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
