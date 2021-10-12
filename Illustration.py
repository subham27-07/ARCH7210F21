import rabbit
import random

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

import rabbit
import random

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
