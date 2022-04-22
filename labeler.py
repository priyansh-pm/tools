import xml.etree.ElementTree as ET
import os
import cv2

files = os.listdir('demo_xmls')
filenumber = len(files)

color = (0, 0, 255)
txt_color = (255, 255, 255)
lw = 2
tf = 1
for i in range(filenumber):
    tree = ET.parse('demo_xmls/' + files[i])
    root = tree.getroot()
    img_name = root[1].text
    im = cv2.imread('demo_imgs/' + img_name)
    for j in range(5, len(root)):
        label = root[j][0].text
        xmin = int(root[j][4][0].text)
        ymin = int(root[j][4][1].text)
        xmax = int(root[j][4][2].text)
        ymax = int(root[j][4][3].text)
        p1, p2 = (xmin, ymin), (xmax, ymax)
        cv2.rectangle(im, p1, p2, color, 2, lineType=cv2.LINE_AA)
        w, h = cv2.getTextSize(label, 0, fontScale=lw / 3, thickness=tf)[0]  # text width, height
        outside = p1[1] - h - 3 >= 0  # label fits outside box
        p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
        cv2.rectangle(im, p1, p2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(im, label, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2), 0, lw / 3, txt_color,
                    thickness=tf, lineType=cv2.LINE_AA)
    cv2.imwrite('done_images/' + img_name, im)
