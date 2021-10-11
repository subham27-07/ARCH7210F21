import rabbit
import random

r=rabbit

# test forward method
r.Drawing.speed = 1
pts = r.Drawing().ptCluster()

print (type(pts))
for pt in pts:
    r.Drawing.rabbit_id = pt
    for j in range (30):
        for i in range (26):
            r.Drawing().forward(i+2)
            r.Drawing.anglexy += i+2
            r.visualization().lineWeight(int(j/10) ,r.visualization().getColorList("gray"))
        r.Drawing.anglez = random.randrange(-20,20)
