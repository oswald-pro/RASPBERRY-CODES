import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

servo = Servo(17)

while True:
  servo.mid()
  print("mid")
  servo.min()
  print("min")
  sleep(1)
  servo.mid()
  print("max")
  sleep(1)
  
