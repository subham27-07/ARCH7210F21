import rabbit
import random
import rhinoscriptsyntax as rs

r=rabbit

# test forward method
# r.Drawing.speed = 1
# pts = r.Drawing().ptCluster()

# print (type(pts))
# for pt in pts:
#     r.Drawing.rabbit_id = pt
#     for j in range (30):
#         for i in range (26):
#             r.Drawing().forward(i+2)
#             r.Drawing.anglexy += i+2
#             r.visualization().lineWeight(int(j/10) ,r.visualization().getColorList("gray"))
#         r.Drawing.anglez = random.randrange(-20,20)

points = r.Drawing().ptCluster()
r.Drawing().irregShape(points)


#Test illustration, will need to modify function
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

        Mirror1(line, list)


myFunc()

####################### Random 3D ####################
####################### Random 3D ####################
####################### Random 3D ####################

def myFunc():

	intLength = rs.GetInteger("how many in x",30)

	intWidth  = rs.GetInteger("how many in y",30)

	intGen	  = rs.GetInteger("how many generations",50)

	strStack  = rs.GetString ("should I stack the generations", "yes", ["yes", "no"])

	arrValues = randomizeArray01(intLength,intWidth)

	arrMeshes = render(arrValues,-1, strStack)

	for i in range(intGen):

		arrValues = applyGOL(arrValues)

		if strStack == "no" :

			update(arrMeshes, arrValues)

		else :

			render(arrValues,i, strStack) 

	

myFunc()


####################### Random 3D ####################
####################### Random 3D ####################
####################### Random 3D ####################
