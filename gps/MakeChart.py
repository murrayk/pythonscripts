'''
Created on 31 Dec 2014

@author: murray
'''



import re
import sys

def _vec2d_dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def _vec2d_sub(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1])


def _vec2d_mult(p1, p2):
    return p1[0]*p2[0] + p1[1]*p2[1]


def ramerdouglas(line, dist):
    """Does Ramer-Douglas-Peucker simplification of a curve with `dist`
    threshold.

    `line` is a list-of-tuples, where each tuple is a 2D coordinate

    Usage is like so:

    >>> myline = [(0.0, 0.0), (1.0, 2.0), (2.0, 1.0)]
    >>> simplified = ramerdouglas(myline, dist = 1.0)
    """

    if len(line) < 3:
        return line

    (begin, end) = (line[0], line[-1]) if line[0] != line[-1] else (line[0], line[-2])

    distSq = []
    for curr in line[1:-1]:
        tmp = (
            _vec2d_dist(begin, curr) - _vec2d_mult(_vec2d_sub(end, begin), _vec2d_sub(curr, begin)) ** 2 / _vec2d_dist(begin, end))
        distSq.append(tmp)

    maxdist = max(distSq)
    if maxdist < dist ** 2:
        return [begin, end]

    pos = distSq.index(maxdist)
    return (ramerdouglas(line[:pos + 2], dist) + 
            ramerdouglas(line[pos + 1:], dist)[1:])


with open('/home/murray/Downloads/blue.tcx') as myfile:
    data=myfile.read().replace('\n', '')
    i = 0
    list = [];
    test=''
    
        
    matches = re.findall("<DistanceMeters>([0-9]+)[.0-9]*</DistanceMeters>.*?<AltitudeMeters>([0-9.]+)</AltitudeMeters>", data)
    del matches[0]
    print len(matches)
        
    myline = []
    for m in matches:
        mytuple = (float(m[0])/1000, float(m[1]) ) 
        myline.append( mytuple)
    
    simplified = ramerdouglas(myline, dist = 0.4)
    print len(simplified)
    for m in simplified:
        print '<item>' + str(m[0]) + ',' + str(m[1]) + '</item>';
        
if __name__ == '__main__':
    pass