'''
Inspired by the Python Turtle library, Rabbit provides a toolkit to generate drawings in Rhinoceros 3D using RhinScriptSyntax. This library is a collaborative effort of students in the Ideas Seminar course in Fall 2021 at the University of North Carolina.
'''

#i think rabbit was a good choice for the name. another animal to add to the list
#test

# Rabbit

#This is a test

import rhinoscriptsyntax as rs
import math
import random

#allObjs = rs.AllObjects()
#rs.DeleteObjects(allObjs)

class Rabbit:
    # mirror the lines if needed
    def mirror(objects, st_point, ed_point):
        for i in range(0, len(objects)):
            if st_point[i][1] > ed_point[i][1]:
                rs.MirrorObject(objects[i], [-1000, 0, 0], [1000, 0, 0])

    # Changing the of scale if required
    def changeScale(points, new_scale):
        for i in range(0, len(points)):
            points[i][0] *= new_scale
            points[i][1] *= new_scale

        return points

    def getColorList(cls):
        color= {
        "red" : [255,0,0],
        "blue" : [0,0,255],
        "green" : [0,255,0],
        "yellow" : [255,185,15],
        "white" : [248,248,255],
        "coral" : [255,127,80],
        "gray" : [166,166,166],
        }
        return color


    # Making curves

    def curve(Val):
        a = []
        for x in range (Val):
            y = math.sin(random.random()*x)
            pt = rs.AddPoint(x,y,0)
            a.append(pt)
