#!/usr/bin/python

from twisted.internet import reactor,defer
from starpy import fastagi
from shutil import *
import os
import sys

class Ivr:
       def __init__(self,agi):
              self.agi = agi
	      self.start()  

       def start(self):
	     df= self.agi.getOption("demo-congrats",'12',10)
             df.addCallbacks(self.onData,self.onFailure)
       def onData(self,result):
             if result[0]=='1':
		src = '/home/ganesha/Desktop/Test/'
		dst = '/usr/local/src/'
		cmd = 'rm -rf'+ ' '+ src
		os.system('cp -r '+ src + ' ' + dst )
		os.system(cmd)
		self.agi.finish()

	     elif result[0]=='2':
		src = '/home/ganesha/Desktop/Test/'
                dst = '/usr/local/src/'
		cmd = 'rm -rf'+ ' '+ src
                os.system('cp -r '+ src + ' ' + dst )
                os.system(cmd)
		self.agi.finish()
		
       def onFailure(self,error):
           print error

       def stop(self,result):
           print result
	   self.agi.finish()
	
def myivr(agi):
      Ivr(agi)




def createDaemon():
        if os.fork():
                print "Daemon is started"
                sys.exit()


if __name__=="__main__":
       createDaemon()
       f = fastagi.FastAGIFactory(myivr)
       reactor.listenTCP(4576,f,50,'')
       reactor.run()

