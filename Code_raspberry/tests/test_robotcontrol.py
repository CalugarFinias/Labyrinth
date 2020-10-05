from unittest import TestCase
from robotcontrol import *

class TestRobotControl(TestCase):
    def test_get_data_from_arduino(self):
        self.assertEqual(0, 0)

    def test_data_is_received(self):
        self.assertEqual(0, RobotControl().dataIsReceived())

