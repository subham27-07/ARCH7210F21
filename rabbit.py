import rhinoscriptsyntax as rs
import math
import random
import Rhino

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
        #def mirror(self, objects, st_point, ed_point):
            #for i in range(0, len(objects)):
                #if st_point[i][1] > ed_point[i][1]:
                   # rs.MirrorObject(objects[i], [-1000, 0, 0], [1000, 0, 0])

        # Changing the of scale if required
            #def changeScale(self, points, new_scale):
                #for i in range(0, len(points)):
                    #points[i][0] *= new_scale
                    #points[i][1] *= new_scale

               # return points
        
    # mirror the lines if needed 
    def Main():

        curve = rs.GetObject("please select a curve",rs.filter.curve)

        line  = rs.GetObject("Select a mirror line")

        pt    = rs.GetObject("please select a point", rs.filter.point)

        limitscale = rs.GetReal("please input a limit scale factor", 0.3)

        angle      = rs.GetReal("please input a rotate angle", 10)

        len        = rs.CurveLength(curve)

        list       = []

        lenlimit=limitscale*len

        while (len>lenlimit):

            if len<=lenlimit: break

            curve = rs.ScaleObject(curve,pt,[0.9,0.9,0.9], True)

            curve = rs.RotateObject(curve,pt,angle)

            len   = rs.CurveLength(curve)

            list.append(curve)

            view = rs.CurrentView()

            rs.ViewCPlane( view, rs.WorldZXPlane() )

            Mirror1(line, list)





    def Mirror1(line, list):

        objs = list

        for i in range(12):

            line1   = rs.RotateObject(line, rs.CurveEndPoint(line), 15, None, copy=False)

            Mirror1 = rs.MirrorObjects( objs, rs.CurveStartPoint(line), rs.CurveEndPoint(line), True )

            list1 = []

            #rs.ScaleObjects(line1, rs.CurveEndPoint(line), [scale, scale, scale], True)

            list1.append(Mirror1)

            line = line1

            #rs.RotateObject( line1, rs.CurveStartPoint(line1), 30, None, True)

            view = rs.CurrentView()

            rs.ViewCPlane( view, rs.WorldYZPlane() )

            rs.HideObjects(line)

            Mirror2(line1, list1)





    def Mirror2(line1, list1):

        objs = list1

        for i in range(12):

            line2 = rs.RotateObject(line1, rs.CurveEndPoint(line1), 15, None, copy=False)

            Mirror2 = rs.MirrorObjects( line1, rs.CurveStartPoint(line1), rs.CurveEndPoint(line1), True )

            list2 = []

            list2.append(Mirror2)

            line1 = line2



            Mirror3(line2, list2, line1)



    def Mirror3(line2, list2, line1):

        objs = list2

        for i in range(15):

            line3 = rs.RotateObject(line2, rs.CurveEndPoint(line2), 15, None, copy=False)

            Mirror3 = rs.MirrorObjects( line2, rs.CurveStartPoint(line2), rs.CurveEndPoint(line2), True )

            list3 = []

            list3.append(Mirror3)

            line2 = line3

            view = rs.CurrentView()

            rs.ViewCPlane( view, rs.WorldZXPlane() )

            RotateMirrors(line1, line2, line3)



    def RotateMirrors(line1, line2, line3):

        rs.RotateObjects( [line1, line2, line3], rs.CurveStartPoint(line3), 30, None, True)

        view = rs.CurrentView()

        rs.ViewCPlane( view, rs.WorldYZPlane() )   
        
    # mirror the lines ends here



    # Making curves
    ### this ones just create the points you might want to crete curves too
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


    # this function creates irregular 3D shapes
    def irregShape(self, points):
        for point in points:
            pt = rs.coerce3dpoint(point)
            # randomely choose how many sides have each shape
            side = random.randrange(7,15)
            # random side size between range(5,20)
            sideSize = random.randrange(5,20)
            # get the corner points 
            pt1 = (pt[0] + sideSize/2, pt[1] + sideSize/2, pt[2] + sideSize/2)
            pt2 = (pt[0] - sideSize/2, pt[1] + sideSize/2, pt[2] + sideSize/2)
            pt3 = (pt[0] + sideSize/2, pt[1] - sideSize/2, pt[2] + sideSize/2)
            pt4 = (pt[0] - sideSize/2, pt[1] - sideSize/2, pt[2] + sideSize/2)
            pt5 = (pt[0] + sideSize/2, pt[1] + sideSize/2, pt[2] - sideSize/2)
            pt6 = (pt[0] - sideSize/2, pt[1] + sideSize/2, pt[2] - sideSize/2)
            pt7 = (pt[0] + sideSize/2, pt[1] - sideSize/2, pt[2] - sideSize/2)
            pt8 = (pt[0] - sideSize/2, pt[1] - sideSize/2, pt[2] - sideSize/2)
            pts = [pt1,pt3,pt4,pt2,pt5,pt7,pt8,pt6]
            # creat the box
            box = rs.AddBox(pts)
            
            breps = []
            for i in range(side-6):
                # get one of the edges to cut from randomely
                centerPt = random.choice(pts)
                # delete the point from list to not being choosen next time
                pts.remove(centerPt)
                # calcualte the vector from the center of the box to the edge
                vector = rs.VectorCreate(centerPt,pt)
                # draw the plan with the calculted vector as normal
                cutPlane = rs.PlaneFromNormal(centerPt,vector)
                # create a circle 
                cutCirc = rs.AddCircle(cutPlane,40)
                # get the line from box center to edge
                curve0 = rs.AddLine(centerPt,pt)
                # get the curve domain
                domain = rs.CurveDomain(curve0)
                # get a point on curve
                midpt = rs.EvaluateCurve(curve0, (domain[0] + (domain[1]/8) + (random.random()*((domain[1]/2)-domain[0]))))
                # draw the extrusion curve
                curve = rs.AddLine(centerPt,midpt)
                # creat a surface
                cutSrf = rs.AddPlanarSrf(cutCirc)
                # extrude surface randomely
                boxCut = rs.ExtrudeSurface(cutSrf,curve)
                originBox = box
                # split the main box to get the new shape
                cube = rs.BooleanDifference(originBox,boxCut)
                # delete all of objects except the main brep
                rs.DeleteObject(cutCirc)
                rs.DeleteObject(curve0)
                rs.DeleteObject(curve)
                rs.DeleteObject(cutSrf)
                rs.DeleteObject(boxCut) 
                if cube:
                    box = cube[0]
                else: 
                    break
            # delete the center points
            rs.DeleteObjects(rs.AddPoint(pt))
                


                
                
                

                
                
                
                
                
    # define maximum canvas constraints
    low = 0; high = 100
    # define range for curves to be created in 
    # "first" is lowest curve
    # "second" is middle curve
    # "third" is top curve
    lowFirst = 0; highFirst = 20
    lowSecond = 34; highSecond = 66
    lowThird = 80; highThird = 100


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
        point_cluster = []

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
            point_cluster.append(rs.AddPoint(point))
        return point_cluster

    # ptCluster()


    #defines multiple points and runs a curve throught them
    def crvThroughPoints():
    
    
    
        #user input for number of points
        input = rs.GetInteger("How many points? ")
    
        vertices = []
    
        #for loop to iterate as many times as the user defined
        for p in range(input):
        
         #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
          #define point with (x,y) coordinates
          #could also add a Z variable and coordinate to make 3d
          point = rs.CreatePoint(ran_number_x,ran_number_y,0)
          #add points to rhino space
          vertices.append(rs.AddPoint(point)) 


        rs.AddCurve(vertices,3)

    #crvThroughPoints()

    
    #draws multiple random curves in 2d using crvThroughPoints function
    def multcurves():
    
    #input to define number of times to run the for loop
        input = rs.GetInteger("How many curves would you like? ")
        
        for i in range(input):
            crvThroughPoints()

    #multcurves()


    #draws random 3d curve
    def crvThroughPoints3d():
        #user input for number of points
        input = rs.GetInteger("How many points? ")
        
        vertices = []
        
        #for loop to iterate as many times as the user defined
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(low, high)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices.append(rs.AddPoint(point)) 


        rs.AddCurve(vertices,3)
        
        
    #crvThroughPoints3d()


    #draws 3 curves in 3d space... one in lower range, one in mid-range, and one in upper range
    #ranges are determined by global variables "low/high first/second/third" 
    def crvThroughRangedPoints3d():
        #user input for number of points per curve
        input = rs.GetInteger("How many points? ")
        
        #setting up variables to be referenced when drawing lines through appended points
        #vertices1 is for curve #1
        #vertices2 is for curve #2
        #vertices3 is for curve #3
        vertices1 = []
        vertices2 = []
        vertices3 = []
        
        #for loop to create first curve in lower range
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowFirst, highFirst)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices1.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        rs.AddCurve(vertices1,3)
        
        #for loop to create first curve in middle range
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowSecond, highSecond)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices2.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        rs.AddCurve(vertices2,3)
        
        #for loop to create first curve in upper range
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowThird, highThird)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices3.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        rs.AddCurve(vertices3,3)
        
    #crvThroughRangedPoints3d()


    #draws 2 curves in 3d space and lofts between them... one curve in upper range and one in lower range
    def loftFrom2():
        #user input for number of points
        input = rs.GetInteger("How many points per curve? ")
        
        vertices1 = []
        
        vertices3 = []
        
        #for loop to iterate as many times as the user defined
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowFirst, highFirst)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices1.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve1 = rs.AddCurve(vertices1,3)
        
        
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowThird, highThird)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices3.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve3 = rs.AddCurve(vertices3,3)
        
        #loft between defined curves
        rs.AddLoftSrf([curve1,curve3])
        
    #loftFrom2()


    #draws 3 curves in 3d space and lofts between them... one curve in upper range, one in mid-range, and one in lower range
    def loftFrom3():
        #user input for number of points
        input = rs.GetInteger("How many points? ")
        
        vertices1 = []
        vertices2 = []
        vertices3 = []
        
        #for loop to iterate as many times as the user defined
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowFirst, highFirst)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices1.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve1 = rs.AddCurve(vertices1,3)
        
        
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowSecond, highSecond)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices2.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve2 = rs.AddCurve(vertices2,3)
        
        
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(low, high)
            #define Y coordinate
            ran_number_y = random.uniform(low, high)
            #define Z coordinate
            ran_number_z = random.uniform(lowThird, highThird)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices3.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve3 = rs.AddCurve(vertices3,3)
        
        #loft between defined curves
        rs.AddLoftSrf([curve1,curve2,curve3])
        
    #loftFrom3()
    

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
    
    def lineWeight(self, printWidth, color):
        '''
        Change the layer of item and its printed width
        '''
        # assign the width to the layers name
        layerName = printWidth
        # create a new layer
        rs.AddLayer(str(layerName), color = None)
        # change the printed width of new layer
        rs.LayerPrintWidth(str(layerName), printWidth)
        # make created layer current
        rs.CurrentLayer(str(layerName))
        # Assign Random color from list
        
    # uses Subhams color creation function "GetcolorList"
    def ranColorSelect(self, getColorList, color):
            ranColorSelect = random.choice(range(getColorList))
            
    # Color by layer, colors layer and all objects in layer
    def colorLayer(self, layerNames, ranColorSelect):
        layerNames = rs.LayerNames()
        if layerNames:
             for name in layerNames: rs.LayerColor(name, ranColorSelect())
        
    
class organization:

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
