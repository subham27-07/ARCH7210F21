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
    
    def Mirror1(self,line, list):
	'''This function takes the line and mirrors it and appends it to list '''
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


    def Mirror2(self,line1, list1):
	'''This function first line and appends it to 2nd list of line and creates mirror'''
        objs = list1
        for i in range(12):
            line2 = rs.RotateObject(line1, rs.CurveEndPoint(line1), 15, None, copy=False)
            Mirror2 = rs.MirrorObjects( line1, rs.CurveStartPoint(line1), rs.CurveEndPoint(line1), True )
            list2 = []
            list2.append(Mirror2)
            line1 = line2
            Mirror3(line2, list2, line1)


    def Mirror3(self,line2, list2, line1):
	'''This function first line and appends it to 3nd list of line and creates mirror'''
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

    def RotateMirrors(self,line1, line2, line3):
        rs.RotateObjects( [line1, line2, line3], rs.CurveStartPoint(line3), 30, None, True)
        view = rs.CurrentView()
        rs.ViewCPlane( view, rs.WorldYZPlane() )   
        
    # mirror the lines ends here
    

    #######################        Generating Lines with Randomness         #####################

	
	def Randomlinegeneration(val):



	    location = [0,0,0] #Initianl Location
	    points=[]

	    for i in range(val):
		x=random.uniform(-1,1)
		y=random.uniform(-1,1)
		z=random.uniform(-1,1)
		point=rs.AddPoint(location[0]+x,location[1]+y,location[2]+z) #specify the location of points
		location=(location[0]+x,location[1]+y,location[2]+z)

		points.append(point)


	    line1=rs.AddCurve(points) #add line to points
	    line= rs.AddPolyline(points) # add curve to points
	    #rs.DeleteObject(points)
		
		#implementing Randomness in color

	    colors = [(193, 0, 0),(5, 46, 192),(146, 75, 96)]
	    color = random.choice(colors)



	    rs.ObjectColor (line, color=color)
	    rs.ObjectColor (line1, color=color)
	    rs.DeleteObject(point)
		
  #######################        Generating Lines with Randomness         #####################



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


    # this function creates irregular 3D shapes
    def irregShape(self, points):
        '''
        Creating irregular shapes based on random number and size of sides from points as inputs
        '''
        # start of the width domain
        WidthS = rs.GetInteger("insert the start number for width domain",minimum = 1)
        # end of the width domain
        WidthE = rs.GetInteger("insert the end number for width domain",minimum = 1)
        # start of the height domain
        HeightS = rs.GetInteger("insert the start number for height domain",minimum = 1)
        # end of the height domain
        HeightE = rs.GetInteger("insert the end number for height domain",minimum = 1)
        
        for point in points:
            pt = rs.coerce3dpoint(point)
            # randomely choose how many sides have each shape
            side = random.randrange(7,15)
            # random side size between range(5,20)
            sideW = random.randrange(WidthS,WidthE)
            sideL = random.randrange(HeightS,HeightE)
            # get the corner points 
            pt1 = (pt[0] + sideL/2, pt[1] + sideL/2, pt[2] + sideW/2)
            pt2 = (pt[0] - sideL/2, pt[1] + sideL/2, pt[2] + sideW/2)
            pt3 = (pt[0] + sideL/2, pt[1] - sideL/2, pt[2] + sideW/2)
            pt4 = (pt[0] - sideL/2, pt[1] - sideL/2, pt[2] + sideW/2)
            pt5 = (pt[0] + sideL/2, pt[1] + sideL/2, pt[2] - sideW/2)
            pt6 = (pt[0] - sideL/2, pt[1] + sideL/2, pt[2] - sideW/2)
            pt7 = (pt[0] + sideL/2, pt[1] - sideL/2, pt[2] - sideW/2)
            pt8 = (pt[0] - sideL/2, pt[1] - sideL/2, pt[2] - sideW/2)
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
                cutCirc = rs.AddCircle(cutPlane,80)
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
        '''Defines a random point in the allowed range, which is based on variables High and Low.'''
        # pick a coordinate in X range
        ran_number_x = random.uniform(self.low, self.high)
        # pick a coordinate in Y range
        ran_number_y = random.uniform(self.low, self.high)

        # define point with (x,y) coordinates
        # could also add a Z variable and coordinate to make 3d
        point = rs.CreatePoint(ran_number_x, ran_number_y, 0)
        # add point to rhino space
        point_id = rs.AddPoint(point)

    
    # defining a a cluster of points in the allowed frame
    def ptCluster(self):
        '''Defines a cluster of points in the allowed range, which is based on variables High and Low.'''
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



    #defines multiple points and runs a curve throught them
    def crvThroughPoints(self):
        '''Defines multiple points and uses them as control points for a curve.'''
        #user input for number of points
        input = rs.GetInteger("How many points? ")
    
        vertices = []

        #for loop to iterate as many times as the user defined
        for p in range(input):
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,0)
            #add points to rhino space
            vertices.append(rs.AddPoint(point)) 
        rs.AddCurve(vertices,3)



    #draws multiple random curves in 2d using crvThroughPoints function
    def multcurves(self):
        '''Draws multiple random curves in 2d by re-triggering crvThroughPoints function a specified number of times.'''
    #input to define number of times to run the for loop
        input = rs.GetInteger("How many curves would you like? ")
        
        for i in range(input):
            crvThroughPoints()



    #draws random 3d curve
    def crvThroughPoints3d(self):
        '''Draws a curve based on multiple points defined in a 3d range, which is based on variables High and Low.'''
        #user input for number of points
        input = rs.GetInteger("How many points? ")
        
        vertices = []
        
        #for loop to iterate as many times as the user defined
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.low, self.high)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices.append(rs.AddPoint(point)) 


        rs.AddCurve(vertices,3)
        
        


    #draws 3 curves in 3d space... one in lower range, one in mid-range, and one in upper range
    #ranges are determined by global variables "low/high first/second/third" 
    def crvThroughRangedPoints3d(self):
        '''Draws three curves in a 3d range... One in a lower range, one in a middle range, and one in an upper range. Ranges are determined by variables High/Low First/Second/Third.'''
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
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowFirst, self.highFirst)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices1.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        rs.AddCurve(vertices1,3)
        
        #for loop to create first curve in middle range
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowSecond, self.highSecond)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices2.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        rs.AddCurve(vertices2,3)
        
        #for loop to create first curve in upper range
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowThird, self.highThird)
            
            #define point with (x,y) coordinates
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices3.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        rs.AddCurve(vertices3,3)
        


    #draws 2 curves in 3d space and lofts between them... one curve in upper range and one in lower range
    def loftFrom2(self):
        '''Draws two curves in a 3d range and lofts between them... One curve in a lower range and one in an upper range. Ranges are determined by variables High/Low First/Second/Third.'''
        #user input for number of points
        input = rs.GetInteger("How many points per curve? ")
        
        vertices1 = []
        
        vertices3 = []
        
        #for loop to iterate as many times as the user defined
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowFirst, self.highFirst)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices1.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve1 = rs.AddCurve(vertices1,3)
        
        
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowThird, self.highThird)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices3.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve3 = rs.AddCurve(vertices3,3)
        
        #loft between defined curves
        rs.AddLoftSrf([curve1,curve3])
        


    #draws 3 curves in 3d space and lofts between them... one curve in upper range, one in mid-range, and one in lower range
    def loftFrom3(self):
        '''Draws three curves in a 3d range and lofts between them... One curve in a lower range, one in a middle range, and one in an upper range. Ranges are determined by variables High/Low First/Second/Third.'''
        #user input for number of points
        input = rs.GetInteger("How many points? ")
        
        vertices1 = []
        vertices2 = []
        vertices3 = []
        
        #for loop to iterate as many times as the user defined
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowFirst, self.highFirst)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices1.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve1 = rs.AddCurve(vertices1,3)
        
        
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowSecond, self.highSecond)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices2.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve2 = rs.AddCurve(vertices2,3)
        
        
        for p in range(input):
            
            #define X coordinate
            ran_number_x = random.uniform(self.low, self.high)
            #define Y coordinate
            ran_number_y = random.uniform(self.low, self.high)
            #define Z coordinate
            ran_number_z = random.uniform(self.lowThird, self.highThird)
            
            #define point with (x,y) coordinates
            #could also add a Z variable and coordinate to make 3d
            point = rs.CreatePoint(ran_number_x,ran_number_y,ran_number_z)
            #add points to rhino space
            vertices3.append(rs.AddPoint(point)) 

        #add curve through points in stored variable
        curve3 = rs.AddCurve(vertices3,3)
        
        #loft between defined curves
        rs.AddLoftSrf([curve1,curve2,curve3])
        


    def ArrayPointsOnSurface(self):
        '''Array a grid of points, defined by the user, across a single selected surface.'''
        # Get the surface object
        surface_id = rs.GetObject("Select surface", rs.filter.surface)
        if surface_id is None: return

        # Get the number of rows
        rows = rs.GetInteger("Number of rows")
        if rows is None: return

        # Get the number of columns
        columns = rs.GetInteger("Number of columns")
        if columns is None: return

        # Get the domain of the surface
        U = rs.SurfaceDomain(surface_id, 0)
        V = rs.SurfaceDomain(surface_id, 1)
        if U is None or V is None: return

        # Add the points
        for i in xrange(0,rows):
            param0 = U[0] + (((U[1] - U[0]) / (rows-1)) * i)
            for j in xrange(0,columns):
                param1 = V[0] + (((V[1] - V[0]) / (columns-1)) * j)
                point = rs.EvaluateSurface(surface_id, param0, param1)
                rs.AddPoint(point)



    # Create organized XY grid of points, arranged along Z axis
    # points grid from coordinate list, points 0 to possibly 40 every 5 units
    def XYZgrid(self):
        '''takes nothing returns points on xyz grid'''
        gridpts = []
        for i in range(0, 100, 10):
            for j in range(0, 100, 10):
                # sets height variable to random integer from 0 to 100
                height = random.choice(range(80))
                point = rs.AddPoint(i, j, height)
                # generates point on xy grid layout and z at random heights
                gridpts.append(point)
                print(type(point))
        return gridpts


    # allObjs = rs.AllObjects()
    # rs.DeleteObjects(allObjs)


    def threeHeightCurves(self):
        '''takes 3 selected returns grid of 3 heigh veriation curves'''
        #Has user select 3 points from rhino model or create and select
        pointA = rs.GetObject("Select point A")
        pointB = rs.GetObject("Select point B")
        pointC = rs.GetObject("Select point C")
        
        pointList = []
        #empty point list   
        axis = []  
        #empty axis list
        for i in range(100):
        #create list of points and store in a 2-dimesional list
            points = []
            for j in range(100):
                points.append(rs.AddPoint(i,j,0))
            pointList.append(points)
            #creates grid of points an adds to 2d list
            
        # draw vertical lines of different length based on proximity to the 3 points. 
        for i in range(len(pointList)):
        #len returns the list length
        #conditional loop, compares point location in grid to one point at a time
            for j in range(len(pointList[i])):
                disA = rs.Distance(pointList[i][j],pointA)
                disB = rs.Distance(pointList[i][j],pointB)
                disC = rs.Distance(pointList[i][j],pointC)
                coords = rs.PointCoordinates(pointList[i][j])
                #sets up parameters for if else statement, grid point cordinates from list, and 3 input points
                if disA < disB and disA<disC:
                    axis.append(rs.AddLine(pointList[i][j],(coords[0],coords[1],35)))
                    #if grid point CLOSEST to pointA, add line height 35
                elif disB<disA and disB < disC:
                    axis.append(rs.AddLine( pointList[i][j],(coords[0],coords[1],40)))
                    #if grid point CLOSEST to pointB, add line height 40
                else:
                    axis.append(rs.AddLine(pointList[i][j] ,(coords[0],coords[1],65)))
                    #if grid point CLOSEST to pointC, add line height 65
                

    def SpheresonPts(self):
        '''takes any collection of points objects or xyz grid function points, returns 3d obect sphere to each'''
        spheres = []
        #add spheres to the gridpts with radius 
        for i in self.gridpts:
            radius = random.choice((0.5,1,1.5,2))
            #in this case if point from gridpts from XYZgrid function, then sphere radious random from list of 4
            #may add perimeter after def, ("name of points host" = gridpts)
            spheres.append(rs.AddSphere(i,radius))
            #spheres organized, made of point and radius 


    def lineform(self):
        '''takes numerical input 3 times, returns lines in form of projected grid and randomized perimeters'''
        List=[]
        #empty list for points
        for i in range(input("input number 3 to 20 for loop iteration of 3d line form:"),50):
            #input gives number for x line layer iteration number start of lines in each, end of range 50
            for j in range(6,30):
                #nested for loop form within form perimeter 6 to 30 for x
                b=random.randint(2,i)
                t=(i,j,0)
                a=(j,i,i)
                #output of i,j in for loops create perimeters for addline
                List.append(t)
                #appends list xy coordinate place
                rs.AddLine(a,t)
                #takes appended coordinates sets as y, takes y from a as x to add line o points

    def xyGrid(self, xNum, yNum):
        '''returns request for input to prints 2d grid'''
        for i in range(xNum):
            for j in range(yNum):
                #sets up for loop, perimeter set up grid x and y
                rs.AddPoint(i, j, 0)
                #point added coordinates x and y no z
        print (xyGrid( input("grid x number:"), input("grid y number:")))
    #for, x and y produced as input x and y organize grid of points 2d
    
    def ObjPoints(self):
        '''takes user selected curve and returns divided curve and points along'''
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
 

    def urchinLines(self):
        '''takes color, count, point, math.pi to return concentric line object'''
        color2 = self.rancolorselect
        color1 = self.rancolorselect 
        #defining 2 colors from rancolorselect function pulling grom getcolorlist in rabbit library
        #can also input list [x,y,z] of numbers ranging 0-255
        count = 0
        step=0
        point = []
        c=pow(2,0.5) #defining root of 2 
        p=math.pi #defining pi value for curves
        
        while count <300: #making interior lines using math
            x = math.cos(random.uniform(-55,55))
            y = math.sin(random.uniform(-55,55))
            z = random.uniform(0,0)
            x1 = random.uniform(-55,55)
            y1 = random.uniform(-55,55)
            z1 = random.uniform(0,0)
            point = (x,y,z)
            #define perimeter first point as 3 coordinate
            point1 = (x1,y1,z1)
            #define perimeter 2nd  point as 3 coordinate
            point2 = (point, point1,(0,0,0))
            #point consist of 2 points as x and y and no z
            
            if rs.Distance(point1,(0,0,0)) > 20 and rs.Distance(point1,(0,0,0)) < 22:
        #condition of curves,distance from center
                a = rs.AddCurve(point2)
                if count>50:
                    rs.ObjectColor(a, color2) #color based on condition greater than 50
                else:
                    rs.ObjectColor(a, color1) #color based on condition less than 50
                count = count + 1
        
        while count < 200: #draw interior lines while color loop iter
            x = math,cos(random.uniform(-55,55))
            y = math.sin(random.uniform(-55,55))
            z = random.uniform(0,0)
            x1 = random.uniform(-55,55)
            y1 = random.uniform(-55,55)
            z1 = random.uniform(0,0)
            point = (x,y,z)
            point1= (x1,y1,z1)
            point2 = (point, point1,(0,0,0))
            if rs.Distance(point, point1,(0,0,0)) > 10 and rs.Distance(point1,(0,0,0)) < 11:
                    rs.AddCurve(point2)
            #interior lines loop concentric, comparison of position to starting points
                    count = count +1

		
    def mandala(self):
        color2 = self.rancolorselect
        color1 = self.rancolorselect
        #defining 2 colors from rancolorselect function pulling grom getcolorlist in rabbit library
        
        count = 0
        step=0
        point = []
        c=pow(2,0.5) #defining root of 2 
        p=math.pi #defining pi value for curves
        
        for d in rs.frange(0.0,(p*input("mandala curve iteration number")),(p/16)): #creating pattern
            x= 15*math.sin(c*d)*math.cos(d)+22.5
            y= 15*math.sin(c*d)*math.sin(d)+22.5
            z= 0
            pt = (x,y,z)
            point.append(pt) #points grouped
        
        sp=rs.AddCurve(point) #grouped points form curve
        rs.ObjectColor(sp, color1) #define color of curve 

	
class visualization:
    
    def getColorList(self,cls):
		'''
		This function is for to get the range of colors
		'''
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
        rs.AddLayer(str(layerName), color)
        # change the printed width of new layer
        rs.LayerPrintWidth(str(layerName), printWidth)
        # make created layer current
        rs.CurrentLayer(str(layerName))
        # Assign Random color from list
        
    
    # uses Subhams color creation function "GetcolorList"
    def ranColorSelect(self, getColorList, color):
	    '''takes Getcolorlist and returns random color selection from'''
            ranColorSelect = random.choice(range(self.getColorList))
            
    # Color by layer, colors layer and all objects in layer
    def colorLayer(self, layerNames, ranColorSelect):
	    '''takes selected layer and returns a color assignment'''
            layerNames = rs.LayerNames()
            if layerNames:
                for name in layerNames: rs.LayerColor(name, self.ranColorSelect)
		#if layername selected for the variable of color, assign the layer name, with rancolor

    def ThreeDscaleObj(self):
        '''takes object and scale factors returns scaled object'''
        rs.ScaleObjects(rs.GetObjects("select obj to scale:"), (0,0,0), (input("input number, x axis scale factor:"), input("input number, y axis scale factor:"),  input("input number, Z axis scale factor:")))
    	#scales user selected object, takes user input for x scale facor y scale factor and z scale factor

    def assignObjColor(self, color):
        '''assigns select object a color'''
	self.ranColorSelect = color
        rs.ObjectColor(rs.GetObjects("select existing obj:"), color)
	    #select object color via random color select    


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
