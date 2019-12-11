'''
Program to run DIY star tracker
Created by Jacob Sommer 2019-10-28
'''
import math
from time import sleep
import asyncio
import RPi.GPIO as GPIO
from multiprocessing import Process
from flask import Flask
from flask import request

# define the ports the IN1-4 for the motor board are connected to
# based on the number coming after GPIO ex: IN1 is connected to port 11/GPIO17 which is 17
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23
DELAY = 0.001
procs = []

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
  return None

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
  return None

@app.route('/drive', methods=['POST'])
def route_drive():
  drive(float(request.form['value']))
  return 'Drive'

@app.route('/turn', methods=['POST'])
def route_turn():
  turn(float(request.form['value']))
  return 'Turn'

@app.route('/stopdrive')
def stop_drive():
  GPIO.output(IN1, False)
  GPIO.output(IN2, False)
  return "Stop drive"

@app.route('/stopturn')
def stop_turn():
  GPIO.output(IN3, False)
  GPIO.output(IN4, False)
  return "Stop turn"

@app.route('/w')
def forward():
  GPIO.output(IN1, False)
  GPIO.output(IN2, True)
  return "Forward"

@app.route('/a')
def left():
  GPIO.output(IN3, False)
  GPIO.output(IN4, True)
  return "Left"

@app.route('/s')
def backward():
  GPIO.output(IN1, True)
  GPIO.output(IN2, False)
  return "Backward"

@app.route('/d')
def right():
  GPIO.output(IN3, True)
  GPIO.output(IN4, False)
  return "Right"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
GPIO.cleanup()