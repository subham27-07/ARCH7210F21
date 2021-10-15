import rabbit
import random
import rhinoscriptsyntax as rs
import math

r=rabbit

# test forward method
def illustration1():
    r.Drawing.speed = 1
    pts = r.Drawing().ptCluster()
    for pt in pts:
        r.Drawing.rabbit_id = pt
        for j in range (10):
            for i in range (10):
                color = (255 * math.cos(j*9 * math.pi / 180), 255 * math.sin(j*9* math.pi / 180),255 *math.cos(j*9* math.pi / 180)* math.sin(j*9* math.pi / 180))
                lineWeight = 0
                lineWeight += ((i+1) * 0.01) + ((j+1) * 0.1)
                r.visualization().lineWeight(lineWeight, color)
                r.Drawing().forward(i+2)
                r.Drawing.anglexy += i
            r.Drawing.anglez += 60
        rs.DeleteObjects(pt) 

# illustration1()

# test forward method
def illustration2():
    r.Drawing.speed = 1
    pts = r.Drawing().ptCluster()
    for pt in pts:
        r.Drawing.rabbit_id = pt
        for j in range (10):
            for i in range (10):
                color = (255 * math.cos(j*3 * math.pi / 180), 255 * math.sin(j*3* math.pi / 180),255 * math.sin(j*3* math.pi / 180))
                lineWeight = 0
                lineWeight += ((i+1) * 0.01) + ((j+1) * 0.1)
                r.visualization().lineWeight(lineWeight, color)
                r.Drawing().forward(i+2)
                r.Drawing.anglexy += i
            r.Drawing.anglez += 45
        rs.DeleteObjects(pt) 
# illustration2()

# test forward method
def illustration3():
    r.Drawing.speed = 1
    pts = r.Drawing().ptCluster()
    for pt in pts:
        r.Drawing.rabbit_id = pt
        for j in range (10):
            for i in range (20):
                color = ((255), 255 * math.sin(j*9* math.pi / 180),255 * math.cos(j*9* math.pi / 180))
                lineWeight = 0
                lineWeight += ((i+1) * 0.01) + ((j+1) * 0.1)
                r.visualization().lineWeight(lineWeight, color)
                r.Drawing().forward(i+2)
                r.Drawing.anglexy += i * 5
                r.Drawing.anglez += 90
        rs.DeleteObjects(pt) 
# illustration3()

def illustration4():
    points = r.Drawing().XYZgrid()
    r.Drawing().irregShape(points)
illustration4()

#Test illustration, will need to modify function
def illustration6():
    location = [0,0,0]
    points=[]

    for i in range(500):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        z=random.uniform(-1,1)
        point=rs.AddPoint(location[0]+x,location[1]+y,location[2]+z)
        location=(location[0]+x,location[1]+y,location[2]+z)
        points.append(point)
    rs.AddCurve(points)
    rs.AddPolyline(points)
# illustration5()


#Test illustration_2, will need to modify function

def myFunc():

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
	colors = [(193, 0, 0),(5, 46, 192),(146, 75, 96)]
        color = random.choice(colors)
        rs.ObjectColor (curve, color=color)
        r.Drawing().Mirror1(line,list)

# myFunc()

####################### Random 3D ####################
####################### Random 3D ####################
####################### Random 3D ####################

def myFunc():
	intLength = rs.GetInteger("how many in x",30)
	intWidth  = rs.GetInteger("how many in y",30)
	intGen	  = rs.GetInteger("how many generations",50)
	strStack  = rs.GetString ("should I stack the generations", "yes", ["yes", "no"])
	arrValues = r.Drawing().randomizeArray01(intLength,intWidth)
	arrMeshes = r.Drawing().render(arrValues,-1, strStack)
	for i in range(intGen):
		arrValues = r.Drawing().applyGOL(arrValues)
		if strStack == "no" :
			r.Drawing().update(arrMeshes, arrValues)
		else :
			r.Drawing().render(arrValues,i, strStack) 


#myFunc()


####################### Random 3D ####################
####################### Random 3D ####################
####################### Random 3D ####################
