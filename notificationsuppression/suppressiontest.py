import time
import os
import yaml
import datetime
from random import randrange

def creation():
    with open(r'timetest.yaml') as rfile:
        violation_list = yaml.load(rfile, Loader=yaml.FullLoader)
    try:
        exceptionhandler = len(violation_list)
    except Exception as e:
        dict_file = {'Time' : 3600}
        with open(r'timetest.yaml', 'w') as wfile:
            documents = yaml.dump(dict_file, wfile)
        

def creator(cam_name,v_type,counter):
    timenow = datetime.datetime.now()
    timenow = int(timenow.strftime("%Y%m%d%H%M%S"))
    with open(r'timetest.yaml') as rfile:
        violation_list = yaml.load(rfile, Loader=yaml.FullLoader)
    if counter == 1:
        violation_list[cam_name][v_type] = timenow        
    else:
        dicts = {}
        dicts[v_type] = timenow
        violation_list[cam_name] = dicts
    with open(r'timetest.yaml', 'w') as wfile:
            documents = yaml.dump(violation_list, wfile)


def checker(cam_name, v_type):
    creation()
    with open(r'timetest.yaml') as rfile:
        violation_list = yaml.load(rfile, Loader=yaml.FullLoader)
    try:
        lastviolationtime = violation_list[cam_name]
        try:
            lastviolationtime = violation_list[cam_name][v_type]
            timenow =  datetime.datetime.now()
            timenow = int(timenow.strftime("%Y%m%d%H%M%S"))
            threshold = violation_list['Time']
            if (timenow-lastviolationtime)>threshold:
                creator(cam_name,v_type,1)
                return True
            else:
                return False
        except Exception:
            creator(cam_name,v_type,1)
            return True
    except Exception:
        creator(cam_name,v_type,0)
        return True

array1 = ['Social Distance','Proximity To dangerous Machines','PPE','Mask','Person Near Edge','Person Under Load','Vehicle Under Load']
for i in range(1,11):
    length = randrange(len(array1))
    print(length)
    cam = 'cam' + str(i)
    for j in range(length):
        fact = checker(cam, array1[j])