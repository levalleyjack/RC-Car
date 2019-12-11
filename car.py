'''
RC Car program for RC League
Created by Jacob Sommer 2019-12-10
'''
import math
from time import sleep
import RPi.GPIO as GPIO
from flask import Flask
from flask import request

# define the ports the IN1-4 for the motor board are connected to
# based on the number coming after GPIO (BCM numbering mode) ex: IN1 is connected to port 11/GPIO17 which is 17
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

# set up GPIO
def setupGPIO():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(IN1, GPIO.OUT)
  GPIO.setup(IN2, GPIO.OUT)
  GPIO.setup(IN3, GPIO.OUT)
  GPIO.setup(IN4, GPIO.OUT)
  GPIO.output(IN1, False)
  GPIO.output(IN2, False)
  GPIO.output(IN3, False)
  GPIO.output(IN4, False)

setupGPIO()

app = Flask(__name__)

def drive(value):
  if value > 0: # forward
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
  elif value < 0: # backward
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
  sleep(math.fabs(value / 100.0))
  GPIO.output(IN1, False)
  GPIO.output(IN2, False)

def turn(value):
  if value > 0: # forward
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
  elif value < 0: # backward
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
  sleep(math.fabs(value / 100.0))
  GPIO.output(IN3, False)
  GPIO.output(IN4, False)

@app.route('/drive', methods=['POST'])
def route_drive():
  drive(float(request.form['value']))
  return 'Drive'

@app.route('/turn', methods=['POST'])
def route_turn():
  turn(float(request.form['value']))
  return 'Turn'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
GPIO.cleanup()