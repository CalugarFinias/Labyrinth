from unittest import TestCase
from robotcontrol import *
from commonOperation import *

class Tests(TestCase):
    def test_data_is_received(self):
        self.assertEqual(0, RobotControl().dataAreReceived())

    def test_wait_data(self):
        waitData()
        self.assertEqual(0, 0)
