import rhinoscriptsyntax as rs
import random


def Mirror1(line, list):
    '''This function takes the line and mirrors it and appends it to list '''

    objs = list

    for i in range(12):

        line1   = rs.RotateObject(line, rs.CurveEndPoint(line), 15, None, copy=False)


        Mirror1 = rs.MirrorObjects( objs, rs.CurveStartPoint(line), rs.CurveEndPoint(line), True )

        list1 = []

        

        list1.append(Mirror1)

        line = line1

        

        view = rs.CurrentView()

        rs.ViewCPlane( view, rs.WorldYZPlane() )

        rs.HideObjects(line)

        Mirror2(line1, list1)





def Mirror2(line1, list1):
    '''This function first line and appends it to 2nd list of line and creates mirror'''

    objs = list1

    for i in range(12):

        line2 = rs.RotateObject(line1, rs.CurveEndPoint(line1), 15, None, copy=False)

        Mirror2 = rs.MirrorObjects( line1, rs.CurveStartPoint(line1), rs.CurveEndPoint(line1), True )

        list2 = []

        list2.append(Mirror2)

        line1 = line2



        Mirror3(line2, list2, line1)



def Mirror3(line2, list2, line1):
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



def RotateMirrors(line1, line2, line3):
    '''This function takes all the lines and creates rotated mirror of the curves'''

    rs.RotateObjects( [line1, line2, line3], rs.CurveStartPoint(line3), 30, None, True)

    view = rs.CurrentView()

    rs.ViewCPlane( view, rs.WorldYZPlane() )
    



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