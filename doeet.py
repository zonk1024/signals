#!/usr/bin/env python
'''
  Just fire 'kill -USR1 <PID>' or 'kill -USR2 <PID>' at it.  It's simple.
'''


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
