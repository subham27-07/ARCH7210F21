import rhinoscriptsyntax as rs
import math
import random

allObjs = rs.AllObjects()
# rs.DeleteObjects(allObjs)


class Drawing:

    # define the general variebles
    # define Home position of rabbit
    rabbit = (0, 0, 0)
    # define rabbit speed
    speed = 1
    # define 2D angle
    anglexy = 0
    # define Third dimention angle
    anglez = 0
    # define the home point
    rabbit_id = rs.AddPoint(rabbit)
    
    
    # mirror the lines if needed
    def mirror(self, objects, st_point, ed_point):
        for i in range(0, len(objects)):
            if st_point[i][1] > ed_point[i][1]:
                rs.MirrorObject(objects[i], [-1000, 0, 0], [1000, 0, 0])

    # Changing the of scale if required
    def changeScale(self, points, new_scale):
        for i in range(0, len(points)):
            points[i][0] *= new_scale
            points[i][1] *= new_scale

        return points



    # Making curves
    def curve(self,Val):
        a = []
        for x in range(Val):
            y = math.sin(random.random()*x)
            pt = rs.AddPoint(x, y, 0)
            a.append(pt)

    # this defenition moves rabbit forward
    def forward(self,value):
        '''
        Real-time drawing in 3D space, toward forward
        '''
        time = 0
        # calculate the time of drawing
        if (value % self.speed == 0):
            time = value / self.speed
        else:
            time = int((float(value) / self.speed)) + 1
        Lines = []
        
        # define the angles (on degree)
        self.anglexy = self.anglexy * math.pi / 180
        self.anglez = self.anglez * math.pi / 180
        
        # drawing the line
        for i in range(time):
            if i == time-1 and value % self.speed !=0 :
                subVal = value % self.speed
            else:
                subVal = self.speed
            # save the start point of the line
            startPt = rs.coerce3dpoint(self.rabbit_id)
            # Calculate the vector
            vector = (subVal * math.cos(self.anglexy) * math.cos(self.anglez), (subVal *math.sin(self.anglexy) * math.cos(self.anglez)), (subVal * math.sin(self.anglez)))
            # move the point to the second position
            self.rabbit_id = rs.MoveObject(self.rabbit_id, vector)
            # save the end point of the line
            endPt = rs.coerce3dpoint(self.rabbit_id)
            # Draw the line
            Lines.append(rs.AddLine(startPt, endPt))
        # Join all of line segments
        curve = rs.JoinCurves(Lines, True)
    
    # this defenition moves rabbit backward
    def backward(self,value):
        '''
        Real-time drawing in 3D space, toward backward
        '''
        # get the variebles that were defined globally
        time = 0
        # calculate the time of drawing
        if (value % self.speed == 0):
            time = value / self.speed
        else:
            time = int((float(value) / self.speed)) + 1
        Lines = []
        
        # define the new angle (on degree)
        self.anglexy = self.anglexy * math.pi / 180
        self.anglez = self.anglez * math.pi / 180
        
        # Draw the  line
        for i in range(time):
            if i == time-1 and value % self.speed !=0 :
                subVal = value % self.speed
            else:
                subVal = self.speed
                
            # save the start point of the line
            startPt = rs.coerce3dpoint(self.rabbit_id)
            # Calculate the vector
            vector = (-subVal * math.cos(self.anglexy) * math.cos(self.anglez), (-subVal *math.sin(self.anglexy) * math.cos(self.anglez)), (-subVal * math.sin(self.anglez)))
            # move the point to the second position
            self.rabbit_id = rs.MoveObject(self.rabbit_id, vector)
            # save the end point of the line
            endPt = rs.coerce3dpoint(self.rabbit_id)
            # Draw the line
            Lines.append(rs.AddLine(startPt, endPt))
        # Join all of line segments
        rs.JoinCurves(Lines, True)

    # define maximum canvas constraints
    low = 0; high = 100

    # defining a random point in the allowed frame
    def randPointInRange(self):
        # pick a coordinate in X range
        ran_number_x = random.uniform(self.low, self.high)
        # pick a coordinate in Y range
        ran_number_y = random.uniform(self.low, self.high)

        # define point with (x,y) coordinates
        # could also add a Z variable and coordinate to make 3d
        point = rs.CreatePoint(ran_number_x, ran_number_y, 0)
        # add point to rhino space
        point_id = rs.AddPoint(point)

    # randPointInRange()
    
    # defining a a cluster of points in the allowed frame
    def ptCluster(self):
        # user input for number of points
        input = rs.GetInteger("How many points? ")

        # for loop to iterate as many times as the user defined
        for p in range(input):

            # define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            # define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)

            # define point with (x,y) coordinates
            # could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x, ran_number_y, 0)
            # add points to rhino space
            point_cluster = rs.AddPoint(point)

    # ptCluster()
    
    # curve from random points
    def crvThroughPoints(self):
        # user input for number of points
        input = rs.GetInteger("How many points? ")

        # for loop to iterate as many times as the user defined
        for p in range(input):

            # define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            # define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            # define point with (x,y) coordinates
            # could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x, ran_number_y, 0)
            # add points to rhino space
            vertices = rs.AddPoint(point)

        rs.AddPolyline(vertices)

    # crvThroughPoints()

    # Create organized XY grid of points, arranged along Z axis
    # points grid from coordinate list, points 0 to possibly 40 every 5 units
    def XYZgrid(self):
        gridpts = []
        for i in range(0, 100, 10):
            for j in range(0, 100, 10):
                # sets height variable to random integer from 0 to 20
                height = random.choice(range(20))
                # generates point on grid layout and at random height
                gridpts.append(rs.AddPoint(i, j, height))

    # allObjs = rs.AllObjects()
    # rs.DeleteObjects(allObjs)
    # divide object(shape or curve) add points
    # Script works without being defined as "def Objpoints():"
    # so not sure why it won't work now, any toughts?
    
    def ObjPoints(self):
        selectObj = rs.GetObject("Select an existing object")
        # divide the object into the number of divisions for points
        ObjDivisions = rs.DivideCurve(
            selectObj, input("select number of divides:"))
        # DivideCurve command generates point objects but doesn't assign a GUID
        # generate a loop to generate GUID's for the points to be used later
        # create an empty list variable for Objpoints
        ObjPoints = []
        # loop through the points and greate a list of GUID's for points
        for Point in ObjDivisions:
            ObjPoints.append(rs.AddPoint(Point))
        print(ObjPoints)
    # allObjs = rs.AllObjects()
    # rs.DeleteObjects(allObjs)

    # Assign Random color from list
    # uses Subhams color creation function "GetcolorList"
        def rancolorselect(getColorList, color):
            rancolorselect=random.choice(range(getColorList))
    # need assignment function


    # Assign to layers
    def CopyObjectsToLayer(self):
        '''
        Copy selected objects to a seperate layer
        '''
        # Get objects to copy
        objectIds=rs.GetObjects("Select objects")
        # Get all layer names
        layerNames=rs.LayerNames()
        if (objectIds == None or layerNames == None): return

        # Make sure select objects are unselected
        rs.UnselectObjects(objectIds)

        layerNames.sort()
        # Get the destination layer
        layer=rs.ComboListBox(
            layerNames, "Destination Layer <" + rs.CurrentLayer() + ">")
        if layer:
            # Add the new layer if necessary
            if(not rs.IsLayer(layer)): rs.AddLayer(layer)
            # Copy the objects
            newObjectIds=rs.CopyObjects(objectIds)

            # Set the layer of the copied objects
            [rs.ObjectLayer(id, layer) for id in newObjIds]
            # Select the newly copied objects
            rs.SelectObjects(newObjIds)

class visualization:
    
    def getColorList(self,cls):
        color = {
        "red": [255, 0, 0],
        "blue": [0, 0, 255],
        "green": [0, 255, 0],
        "yellow": [255, 185, 15],
        "white": [248, 248, 255],
        "coral": [255, 127, 80],
        "gray": [166, 166, 166],
        }
        return color