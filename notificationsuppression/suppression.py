import datetime
import yaml

class suppressor:
    def __init__(self, cam_name, v_type):
        self.cam_name = cam_name
        self.v_type = v_type

    def creation(self):
        with open('time.yaml', 'r', encoding='utf-8') as rfile:
            violation_list = yaml.load(rfile, Loader=yaml.FullLoader)
        try:
            len(violation_list)
        except TypeError:
            dict_file = {'Time' : 3600}
            with open(r'time.yaml', 'w', encoding='utf-8') as wfile:
                yaml.dump(dict_file, wfile)

    def creator(self,counter):
        timenow = datetime.datetime.now()
        timenow = int(timenow.strftime("%Y%m%d%H%M%S"))
        with open(r'time.yaml', 'r', encoding='utf-8') as rfile:
            violation_list = yaml.load(rfile, Loader=yaml.FullLoader)
        if counter == 1:
            violation_list[self.cam_name][self.v_type] = timenow
        else:
            dicts = {}
            dicts[self.v_type] = timenow
            violation_list[self.cam_name] = dicts
        with open(r'time.yaml', 'w', encoding='utf-8') as wfile:
            yaml.dump(violation_list, wfile)

    def checker(self):
        self.creation()
        with open(r'time.yaml', 'r', encoding='utf-8') as rfile:
            violation_list = yaml.load(rfile, Loader=yaml.FullLoader)
        try:
            lastviolationtime = violation_list[self.cam_name]
            try:
                lastviolationtime = violation_list[self.cam_name][self.v_type]
                timenow =  datetime.datetime.now()
                timenow = int(timenow.strftime("%Y%m%d%H%M%S"))
                threshold = violation_list['Time']
                if (timenow-lastviolationtime)>threshold:
                    self.creator(1)
                    return True
                return False
            except KeyError:
                self.creator(1)
                return True
        except KeyError:
            self.creator(0)
            return True
