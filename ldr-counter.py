#!/usr/bin/python

# Reading an analogue sensor with  a single GPIO pin

# Basic script from:
# /www.raspberrypi-spy.co.uk/2012/08/reading-analogue-sensors-with-one-gpio-pin/
# Author : Matt Hawkins  -- Stephen Pratt (SJP)
# Distribution : Raspbian -- SJP Arch-arm
# Python : 2.7 -- SJP converted to v3.5
# GPIO   : RPi.GPIO v3.1.0a

# PIN assignments:
#   pin     Name        Connection
#   1       +3.3V       power source
#   7       GPIO 4      read sensor
#   9       Ground      Ground

# circuit characteristics
#   series resistor             = 220 Ohm
#   LDR resistance (full sun)   = 360 Ohm
#                   'dusk'      =   3 M Ohm
#   capactitor                  = 10 uF (quite large)
#   max current = 3.3/580       = 5.7 mA (well within spec)

import RPi.GPIO as GPIO, time

# set GPIO4 as read pin
sensorPin = 4
# set maximum time to wait (in which case it is dark)
maxWait = 5e6
obsCount = 6    # number of observations

# Tell the GPIO library to use Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

# Define function to measure charge time
def RCtime ():
  timer = 0
  # Discharge capacitor
  GPIO.setup(sensorPin, GPIO.OUT)
  GPIO.output(sensorPin, GPIO.LOW)
  time.sleep(0.1)           # 100 ms

  GPIO.setup(sensorPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(sensorPin) == GPIO.LOW):
    timer += 1
    if timer > maxWait : return -1
  return timer

# Main program loop
obs=list()      # an empty list
for num in range(0, obsCount):
    obs.append(RCtime())
    print(obs)
print("sum=", sum(obs))
print("Ave time: ", sum(obs)/obsCount)        # Measure timing using GPIO4
