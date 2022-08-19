import cv2
import numpy as np
from shapely.geometry import Polygon, Point


def polypointchecker(ppllist,conelist,frame):
    poly = Polygon(conelist)
    violation_count = 0
    for i in range(len(ppllist)):
        if poly.contains(Point(ppllist[i])):
            cv2.circle(frame,(int(ppllist[i][0]),int(ppllist[i][1])),3,(0,0,255),-1)
            violation_count = violation_count + 1
    return violation_count,frame

img = cv2.imread('blank_image.png')
imgcopy = img.copy()
print(img.shape)
list = [[10, 50], [2, 160], [11, 200], [20, 160], [200, 70], [110, 240]]
xmid = []
ymid = []
for i in range(len(list)):
    cv2.circle(img, (list[i][0], list[i][1]), 5, (0, 0, 255), -1)
    cv2.putText(img, f'{list[i][0]},{list[i][1]}', (list[i][0]+10, list[i][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    xmid.append(list[i][0])
    ymid.append(list[i][1])

def midpt(xlist,ylist):
    xtot = 0
    ytot = 0
    for i in range(len(xlist)):
        xtot = xtot + xlist[i]
        ytot = ytot + ylist[i]
    xmid = xtot/len(xlist)
    ymid = ytot/len(ylist)
    return xmid, ymid

midpts = midpt(xmid, ymid)
cv2.circle(img, (int(midpts[0]), int(midpts[1])), 5, (0, 255, 0), -1)

def angle(x,y,midpt):
    angle = np.arctan2(y-midpt[1], x-midpt[0])
    return angle

anglelist = []
for i in range(0, len(list)):
    x = list[i][0]
    y = list[i][1]
    anglelist.append(angle(x, y, midpts))

totalist = []
for i in range(0, len(anglelist)):
    totalist.append([anglelist[i],list[i]])

sortlist = sorted(totalist)
sortcoords = []
for i in range(0, len(sortlist)):
    cv2.line(img,(sortlist[i][1][0],sortlist[i][1][1]),(sortlist[(i+1)%len(sortlist)][1][0],sortlist[(i+1)%len(sortlist)][1][1]),(0,255,0),2)
    sortcoords.append((sortlist[i][1][0],sortlist[i][1][1]))
imgc = img.copy()
imgsc = cv2.fillPoly(imgc, np.array([sortcoords]), (0, 255, 0))

a = 150
b = 210
p1 = Point(a, b)
poly = Polygon(sortcoords)
polyz = Polygon(list)

img = cv2.circle(img, (a, b), 5, (255, 0, 0), -1)
print(p1.within(poly))
print(p1.within(polyz))
print(polyz)
cv2.imwrite('image.png', img)
cv2.imwrite('image_sc.png', imgsc)
