import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

HOOK = 22
DIAL = 27
TIMEOUT_PERIOD = 4

GPIO.setup(HOOK, GPIO.IN)

while true:
  dialCount=0
  dialDialing=false
  dialState=
  dialTime=time.time()
  playing=false
  while not GPIO.input(HOOK):
    if not playing:
      newState = GPIO.input(DIAL)
      if newState != dialState:
	++dialCount
	dialCount=0
	dialTime=time.time()
	dialState = newState
      if dialDialing and ((dialTime + TIMEOUT_PERIOD) > time.time()):
	print "you dialed " + (dialCount - 3)
	playing=true

  