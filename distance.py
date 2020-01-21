'''
Program for measuring distance between two points using a GPS connected to a Raspberry Pi
Author: Jack LeValley
Date: 2020-01-20
'''
from geopy.distance import distance

# print(distance((37.7749, -122.4194), (40.7128, -74.0060)).miles)
print(distance((37.72127583333334, -121.92477566666666), (37.72127666666667, -121.9247765)).feet)