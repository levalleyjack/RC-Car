'''
Program for reading and parsing data from a GPS connected to the Raspberry Pi serial pins
Author: Jacob Sommer
Date: 2020-01-20
'''
import time
import serial
import pynmea2

def parseGPS(str):
  '''
  Parses the raw GPS data using pynmea2
  '''
  if 'GGA' in str: # the line containing all of the GPS data is identified by GPGGA in which GGA is unique to that line
    msg = pynmea2.parse(str)
    print("Timestamp: %s -- Lat: %s -- Lon: %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.latitude, msg.longitude, msg.altitude, msg.altitude_units, msg.num_sats))
    # print("Timestamp: %s -- Lat: %02d°%02d′%07.4f″ -- Lon: %02d°%02d′%07.4f″ -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.latitude, msg.latitude_minutes, msg.latitude_seconds, msg.longitude, msg.longitude_minutes, msg.longitude_seconds, msg.altitude, msg.altitude_units, msg.num_sats))

# creates a new serial object and listens to the GPIO serial pins
ser = serial.Serial(
  port='/dev/ttyS0', # port for reading from GPIO serial pins
  baudrate = 9600, # 9600 baud (bits per second)
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

while 1: # infinite loop, constantly reads and parses GPS data
  parseGPS(ser.readline().decode()) # use decode to convert from bytes to string