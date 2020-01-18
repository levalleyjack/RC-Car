import time
import serial
import pynmea2

def parseGPS(str):
  if 'GGA' in str:
    msg = pynmea2.parse(str)
    print("Timestamp: %s -- Lat: %s -- Lon: %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.latitude, msg.longitude, msg.altitude, msg.altitude_units, msg.num_sats))
    print("Timestamp: %s -- Lat: %02d°%02d′%07.4f″ -- Lon: %02d°%02d′%07.4f″ -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.latitude, msg.latitude_minutes, msg.latitude_seconds, msg.longitude, msg.longitude_minutes, msg.longitude_seconds, msg.altitude, msg.altitude_units, msg.num_sats))

ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

while 1:
  parseGPS(ser.readline().decode()) # use decode to convert from bytes to string