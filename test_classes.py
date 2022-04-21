import pytest
from classes import *


class Test:
    def setup_method(self):
        self.t1 = Television()
        self.t2 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert self.t1.get_status() is False
        assert self.t1.get_channel() == 0
        assert self.t1.get_volume() == 0

        assert self.t2.get_status() is False
        assert self.t2.get_channel() == 0
        assert self.t2.get_volume() == 0

    def test_power(self):
        self.t1.power()
        assert self.t1.get_status() is True

        self.t2.power()
        self.t2.power()
        assert self.t2.get_status() is False

