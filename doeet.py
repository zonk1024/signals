#!/usr/bin/env python

import signal
import time

def handler(signum, frame):
    print int(time.time())

signal.signal(signal.SIGUSR1, handler)

def handler2(signum, frame):
    print int(time.time())
    exit(0)

signal.signal(signal.SIGUSR2, handler2)

while True:
    pass
