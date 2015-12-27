import RPi.GPIO as GPIO
import time
from pygame import mixer
GPIO.setmode(GPIO.BCM)

HOOK = 22
DIAL = 27
TIMEOUT_PERIOD = 3

GPIO.setup(HOOK, GPIO.IN)
GPIO.setup(DIAL, GPIO.IN)
mixer.init()
while 1:
  dialCount=0
  dialDialing=0
  dialState=GPIO.input(DIAL)
  dialTime=time.time()
  playing=0
  while not GPIO.input(HOOK):
    
    if not playing:
      newState = GPIO.input(DIAL)
      if newState != dialState:
	print "state change"
	dialCount = dialCount + 1
	dialTime=time.time()
	dialState = newState
	dialDialing=1
      if dialDialing and ((dialTime + TIMEOUT_PERIOD) < time.time()):
	dialed = ((dialCount / 2) -1)
	print "you dialed %d" % dialed
	playing=1
	mixer.music.load("%d.mp3" % (dialed))
	mixer.music.play()
  mixer.music.stop() 

  
