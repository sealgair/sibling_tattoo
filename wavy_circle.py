#! /usr/local/bin/python
import sys
from math import cos, sin, pi
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
origin = Point(50, 50)
apexes = [3, -2]

def make_path(radius, steps):
    steps = float(steps)
    path = "M {} {}".format(origin.x+radius, origin.y)
    
    for i in range(1, int(steps)+1):
        i = float(i)
        t = (pi/2) * (i/steps)
        end = Point(origin.x+cos(t)*radius, origin.y-sin(t)*radius)
        t -= (pi/2)/(2*steps)
        r2 = radius + apexes[int(i%2)] 
        mid = Point(origin.x+cos(t)*r2, origin.y-sin(t)*r2)
        
        path += " Q {mid.x:.2f} {mid.y:.2f} {end.x:.2f} {end.y:.2f}".format(
            mid=mid, end=end
        )
    print path

if __name__ == "__main__":
    make_path(int(sys.argv[1]), int(sys.argv[2]))
