import os
import xml.etree.ElementTree as ET
import cv2

files = os.listdir('imgdata/xmls/')
print(files)
numfiles = len(files)

for i in range(0, numfiles):
    tree = ET.parse('imgdata/xmls/' + files[i])
    root = tree.getroot()
    print("ROOT LENGTH = ", len(root))
    imagename = root[1].text
    img = cv2.imread('imgdata/imgs/' + imagename)
    for j in range(5, len(root)):
        xmin = root[j][4][0].text
        print(xmin)
        ymin = root[j][4][1].text
        print(ymin)
        xmax = root[j][4][2].text
        print(xmax)
        ymax = root[j][4][3].text
        print(ymax)
        cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 4)
    cv2.imwrite('imgdata/madeimgs/vios' + str(i) + '.jpg', img)