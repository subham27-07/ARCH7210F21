import rhinoscriptsyntax as rs
import math

# define Home position of rabbit
rabbit = (0,0,0)
# define rabbit speed
speed = 1
# define 2D angle
angle1 = 0
# define Thrid dimention angle 
angle2 = 0
rabbit_id = rs.AddPoint(rabbit)

# this defenition moves rabbit forward
def forward(value):
    # get the variebles that were defined globally
    time = 0
    # calculate the time of drawing
    if (isinstance((value / speed), int)):
        time = value / speed
    if (isinstance((value / speed), float)):
        time = int((value / speed)) + 1
    Lines = []
    # Draw the  line
    for i in range (time):
        # save the start point of the line
        print(rabbit_id)
        startPt = rs.coerce3dpoint(rabbit_id)
        # Calculate the vector 
        vector =  ((value * math.cos(angle1)* math.cos(angle2)/time),(value * math.sin(angle1)* math.cos(angle2)/time),(value * math.sin(angle2)/time))
        # move the point to the second position
        rabbit_id = rs.MoveObject(rabbit_id, vector)
        # save the end point of the line
        endPt = rs.coerce3dpoint(rabbit_id)
        # Draw the line
        Lines.append ( rs.AddLine(startPt,endPt))
    # Join all of line segments
    rs.JoinCurves(Lines, True)

# this defenition moves rabbit forward
def backward(value): 
    # get the variebles that were defined globally

    time = 0
    # calculate the time of drawing
    if (isinstance((value / speed), int)):
        time = value / speed
    if (isinstance((value / speed), float)):
        time = int((value / speed)) + 1
    Lines = []
    # Draw the  line
    for i in range (time):
        # save the start point of the line
        startPt = rs.coerce3dpoint(rabbit_id)
        # Calculate the vector 
        vector =  (-(value * math.cos(angle1)* math.cos(angle2)/time),-(value * math.sin(angle1)* math.cos(angle2)/time),-(value * math.sin(angle2)/time))
        rabbit_id = rs.MoveObject(rabbit_id,vector)
        # save the end point of the line
        endPt = rs.coerce3dpoint(rabbit_id)
        # save the end point of the line
        Lines.append ( rs.AddLine(startPt,endPt))
    # Join all of line segments
    rs.JoinCurves(Lines, True)

# This definition defines the angle of rotation in a 2D space
def right(value): 
    # Get the global varieble
    global angle1
    # define the new angle (on degree)
    angle1 = angle1 + (- value * math.pi / 180)
    
# This definition defines the angle of rotation in a 2D space
def left(value): 
    # Get the global varieble
    global angle1
    # define the new angle (on degree)
    angle1 = angle1 + (value *  math.pi / 180)
    
# This definition defines the angle of rotation in a 3D space  
def up(value): 
    # Get the global varieble
    global angle2 
    # define the new angle (on degree)
    angle2 = angle2 +( value *  math.pi / 180)
# This definition defines the angle of rotation in a 3D space
def down(value): 
    # Get the global varieble
    global angle2 
    # define the new angle (on degree)
    angle2 = angle2 + (- value * math.pi / 180)


#test the function
for i in range (4):
    forward(10)
    left(40)
    forward(20)
    right(30)
    forward(30)
    up(10)
    forward(30)
    left(30)