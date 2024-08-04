#!/usr/bin/python3
"""log parsing"""
import sys
import signal
import re
from collections import OrderedDict


logs = {}


def print_stat():
    """to print stats"""
    size = logs.get("Filesize")
    if (size is not None) and (size != 0):
        sortlog = OrderedDict(sorted(logs.items()))
        print(f"File size: {logs.get('Filesize')}")
        printcpt = 0
        for key, value in sortlog.items():
            if key != "Filesize":
                print(f"{key}: {value}")
                printcpt = printcpt + 1
                if printcpt == 10:
                    break


def handler(signum, frame):
    """Ctr + C handler"""
    print_stat()


def addtologs(numbers):
    """add stats"""
    if len(numbers) >= 2:
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
print_stat()
