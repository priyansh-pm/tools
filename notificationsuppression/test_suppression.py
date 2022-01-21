import unittest
import yaml
from notificationsuppression.suppression import suppressor


def checkforsuppression(filename):
    with open(filename, 'r', encoding='utf-8') as rfile:
        test_list = yaml.load(rfile, Loader=yaml.FullLoader)
    camera = [*test_list]
    cameralist = len(camera)
    checkerbooleanlist = []
    for i in range(0,cameralist):
        violation = [*test_list[camera[i]]]
        violationlist = len(violation)
        for j in range(0,violationlist):
            timeforsend = test_list[camera[i]][violation[j]]
            test = suppressor(camera[i], violation[j], timeforsend)
            checkerbooleanlist.append(test.checker())
    return checkerbooleanlist

class TestSuppression(unittest.TestCase):
    def test_suppression_success(self):
        test1 = checkforsuppression('notificationsuppression/timetest.yaml')
        anstest1 = [False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.assertEqual(test1, anstest1)

    def test_suppression_success2(self):
        test2 = checkforsuppression('notificationsuppression/timetesttrue.yaml')
        anstest2 = [True, True, False, False, True, False, True, False, False, False, True,
        False, False, False, False, False, False, False, True, True, False, True, True,
        False, False, False, True, True, False, False, True, True, False, True, False, False,
        False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True]
        self.assertEqual(test2, anstest2)
