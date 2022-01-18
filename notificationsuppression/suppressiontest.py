from random import randrange
from suppression import suppressor

array1 = ['SD','Proximity','PPE','Mask','Person Near Edge','Person Under Load','Vehicle']
for i in range(1,11):
    length = randrange(len(array1))
    print(length)
    cam = 'cam' + str(i)
    for j in range(length):
        fact = suppressor(cam, array1[j])
        fact.checker()
