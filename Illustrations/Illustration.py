import rhinoscriptsyntax as rs
import random

def Randomlinegeneration(val):
    '''This function generates the points randomly in x,y,z axis and joins them through lines and curves'''

    location = [ 0,0,0]
    points=[]
    
    for i in range(val):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        z=random.uniform(-1,1)
        point=rs.AddPoint(location[0]+x,location[1]+y,location[2]+z)
        location=(location[0]+x,location[1]+y,location[2]+z)
        
        points.append(point)
        
    
        
    line1=rs.AddCurve(points)
    line= rs.AddPolyline(points)
    
    #assigning random colors to the generated lines & curves
    colors = [(193, 0, 0),(5, 46, 192),(146, 75, 96)]
    color = random.choice(colors)
    rs.ObjectColor (line, color=color)
    rs.ObjectColor (line1, color=color)
    
    #rs.DeleteObject(points)
    rs.DeleteObjects(points)

x= input('Enter value of nos. of points to generate the lines')


Randomlinegeneration(x)
#Run the program several times to see the change and get an illustration