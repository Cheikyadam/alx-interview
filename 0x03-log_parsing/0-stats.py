#!/usr/bin/python3
"""log parsing"""
import sys
import signal
import re
from collections import OrderedDict


logs = {}


def print_stat():
    """to print stats"""
    if logs.get("Filesize") is not None:
        sortlog = OrderedDict(sorted(logs.items()))
        print(f"File size: {logs.get('Filesize')}")
        for key, value in sortlog.items():
            if key != "Filesize":
                print(f"{key}: {value}")


def handler(signum, frame):
    """Ctr + C handler"""
    print_stat()


def addtologs(numbers):
    """add stats"""
    oldsize = logs.get("Filesize")
    if oldsize is None:
        oldsize = 0
    logs['Filesize'] = oldsize + int(numbers[1])
    oldcode = logs.get(numbers[0])
    if oldcode is None:
        oldcode = 0
    logs[numbers[0]] = oldcode + 1


cpt = 0
signal.signal(signal.SIGINT, handler)
for line in sys.stdin:
    numbers = re.findall(r'\d+', line)
    addtologs(numbers[-2:])
    cpt = cpt + 1
    if cpt == 10:
        print_stat()
        cpt = 0
        logs = {}

