import os
import cv2

a = os.listdir('Test/WithoutMask')
b = os.listdir('Test/WithMask')
c = os.listdir('Validation/WithoutMask')
d = os.listdir('Validation/WithMask')

linemask = '1 0.500000 0.500000 1.000000 1.000000'
linewithoutmask = '0 0.500000 0.500000 1.000000 1.000000'

print("Full set : ", (len(a) + len(b) + len(c) + len(d)))
counter = 1

for i in range(len(a)):
    img = cv2.imread('Test/WithoutMask/' + a[i])
    cv2.imwrite('all/' + str(counter) + '.jpg', img)
    f = open('textfile/' + str(counter) + '.txt', 'w')
    f.write(linewithoutmask)
    f.close()
    print(counter)
    counter += 1

for i in range(len(b)):
    img = cv2.imread('Test/WithMask/' + b[i])
    cv2.imwrite('all/' + str(counter) + '.jpg', img)
    f = open('textfile/' + str(counter) + '.txt', 'w')
    f.write(linemask)
    f.close()
    print(counter)
    counter += 1

for i in range(len(c)):
    img = cv2.imread('Validation/WithoutMask/' + c[i])
    cv2.imwrite('all/' + str(counter) + '.jpg', img)
    f = open('textfile/' + str(counter) + '.txt', 'w')
    f.write(linewithoutmask)
    f.close()
    print(counter)
    counter += 1

for i in range(len(d)):
    img = cv2.imread('Validation/WithMask/' + d[i])
    cv2.imwrite('all/' + str(counter) + '.jpg', img)
    f = open('textfile/' + str(counter) + '.txt', 'w')
    f.write(linemask)
    f.close()
    print(counter)
    counter += 1