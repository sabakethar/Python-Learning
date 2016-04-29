#! /usr/bin/python

import threading, time

class Thread(threading.Thread):
    def run(self):
        while(1):
            print("in thread")
            time.sleep(3)

def main():
    t=Thread()
    t.start()

    while(1):
        print("in main")
        time.sleep(5)

main()

