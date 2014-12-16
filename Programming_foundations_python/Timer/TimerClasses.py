# -*- coding=utf-8 -*-
import webbrowser
import time


class Timer():
    def __init__(self, video='', time_sleep=60*60*2):
        self.video = video
        self.time  = time_sleep

    def launchVideo(self,time_sleep=None):
        if isinstance(time_sleep, int):
            self.time = time_sleep
        time.sleep(self.time)
        webbrowser.open(self.video)

    def startTimer(self):
        for x in range(1,4):
            print "Time %d" % x
            self.launchVideo(3)
    def main(self):
        self.startTimer()

if __name__ == '__main__':
    t = Timer("http://vimeo.com/93003441")
    t.main()