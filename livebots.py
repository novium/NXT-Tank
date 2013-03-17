import sys
import grabber
import urllib2
import serial
import threading

class message:
    def __init__(self, defaultUrl, robotId):
        self.url = defaultUrl + robotId + '.html'
        print(self.url)
        self.string = ''

    def request(self):
        req = urllib2.Request(self.url)
        response =  urllib2.urlopen(req)
        html = response.read()
        html=html.strip()
        html=html.rstrip()
        html=html.lstrip()
        self.string = str(html)
        return self.string

class robot:
    def send(self, message):
        if message == 'Forward':
            grabber.forward()
        elif message == 'Backward':
            grabber.backward()
        elif message == 'Right':
            grabber.right()
        elif message == 'Left':
            grabber.left()
        else:
            print('Unknown message: ' + message)


class livebot:     
    def __init__(self, robotId):
        self.msg = message('http://livebots.cc/Robot/Message/', robotId)
        self.bot = robot()
        self.lastMessage = ''
        self.loop()
        
    def loop(self):
        threading.Timer(1, self.loop).start()
        message = self.msg.request()
        if message != self.lastMessage:
            print(message)
            try:
                self.bot.send(message.split()[0])
            except:
                print "Unexpected error:", sys.exc_info()
                pass
            self.lastMessage = message
