#! /usr/bin/python

# This script is based on GPS Python example Written by Dan Mandle http://dan.mandle.me September 2012
# The main pourpouse of my modification, is to Log GPS position info flat file
# later to be used to track the position of Wifi Client devices like Phones and Laptops
# compared against Airodump CSV file output.
# -This script only captures the GPS data, and is not processing any Airodump output.
# T.D. http://www.dobrotka.sk, 17.1.2015
# https://github.com/ggtd/independend-python-gps-logger-for-airodump-ng

# -----------------Original credits ------------
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading
import datetime
from time import gmtime, strftime


 
gpsd = None #seting the global variable

time1= None
time2= "placeholder string"

os.system('clear') #clear the terminal (optional)

flog = open('./gps_log_file', 'a')
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      time1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc

      os.system('clear')

      print
      print ' GPS reading + Logging'
      print '----------------------------------------'
      print 'latitude    ' , gpsd.fix.latitude
      print 'longitude   ' , gpsd.fix.longitude
      print 'time utc    ' , gpsd.utc
      print
      print 'time1:', time1
      print 'time2:', time2


      if (time1+"" != time2+""): # Check if Second tick changed, if yes, log possiton
	print "Log time!"
	time2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	log_string=str(time1)+":"+str(gpsd.fix.latitude)+" "+str(gpsd.fix.longitude)+"\n"
	flog.write(log_string)
      time.sleep(0.4)

 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
  
