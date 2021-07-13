from unittest import TestCase
from test_python_code.src.gewen import Gewen
from test_python_code.src.mengduo import Mengduo


class Testhero(TestCase):
    def test_fight(self):
        mengduo = Mengduo()
        gewen = Gewen()
        assert mengduo.fight(gewen) == True
        mengduo = Mengduo()
        gewen = Gewen()
        assert gewen.fight(mengduo) == False
