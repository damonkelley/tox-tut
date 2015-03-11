import os

def is_odd(n):
    return n%2 == 1


def print_me():
    print os.environ.get("USER")
