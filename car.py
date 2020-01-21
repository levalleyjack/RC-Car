'''
Program for controlling an RC Car through POST requests
Created by Jacob Sommer 2020-01-20
'''
import math
from time import sleep
import RPi.GPIO as GPIO
from flask import Flask
from flask import request

# define the ports the IN1-4 for the motor board are connected to
# based on the number coming after GPIO (BCM numbering mode) ex: IN1 is connected to port 11/GPIO17 which is 17
IN1 = 26
IN2 = 19
IN3 = 13
IN4 = 6
PWM1 = 21
PWM2 = 20

# constants for maximum motor speed (up to 100)
DRIVE_SPEED = 100
TURN_SPEED = 100

# set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(PWM2, GPIO.OUT)
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)
drive_pwm = GPIO.PWM(PWM1, 100)
turn_pwm = GPIO.PWM(PWM2, 100)
drive_pwm.start(DRIVE_SPEED)
turn_pwm.start(TURN_SPEED)


def drive(value):
  '''
  Drive at the specified speed in the specified direction
  value - float between -1 and 1, raw input value
  '''
  if value > 0: # forward
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    drive_pwm.ChangeDutyCycle(int(DRIVE_SPEED * value))
  elif value < 0: # backward
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    drive_pwm.ChangeDutyCycle(int(DRIVE_SPEED * -value))
  else:
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def turn(value):
  '''
  Turn at the specified speed in the specified direction
  value - float between -1 and 1, raw input value
  '''
  if value > 0: # forward
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    turn_pwm.ChangeDutyCycle(int(TURN_SPEED * value))
  elif value < 0: # backward
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    turn_pwm.ChangeDutyCycle(int(TURN_SPEED * -value))
  else:
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

app = Flask(__name__) # create Flask app object

@app.route('/drive', methods=['POST'])
def route_drive():
  '''
  Listen for POST requests to /drive and process them
  '''
  drive(float(request.form['value']))
  return 'Drive'

@app.route('/turn', methods=['POST'])
def route_turn():
  '''
  Listen for POST requests to /turn and process them
  '''
  turn(float(request.form['value']))
  return 'Turn'

if __name__ == '__main__': # if this file is launched directly
  app.run(host='0.0.0.0', debug=True, port=5000) # run Flask app
GPIO.cleanup() # clean up GPIO pins after app closed
