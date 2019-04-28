"""
A) Write a program that shows the status of the current traffic-light
B) Extend the previous program to ask for user interaction
"""

from time import sleep
from random import randint

# traffic-light constants in seconds
# QUESTIONS: does the random generator include or exclude the limits?
MIN_WAIT = 5.0
MAX_WAIT = 10.0


def red():
    print('RED')
    sleep(randint(MIN_WAIT, MAX_WAIT))


def yellow():
    print('YELLOW')
    sleep(3)


def green():
    print('GREEN')


def go():
    pass


while True:
    red()
    yellow()
    green()
    go()
