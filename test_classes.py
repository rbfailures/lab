import pytest
from classes import *


class Test:
    def setup_method(self) -> None:
        """
        Setup method for testing
        :return: None
        """
        self.t1 = Television()

    def teardown_method(self) -> None:
        """
        Teardown method for testing
        :return: None
        """
        del self.t1

    def test_init(self) -> None:
        """
        Tests if the __init__ function of class Television initializes object with correct values
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    def test_power(self) -> None:
        """
        Tests that the power method of Television Class works as intended
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.t1.power()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    def test_channel_up(self) -> None:
        """
        Tests that the channel_up method of Television Class works as intended
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.t1.power()
        self.t1.channel_up()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"
        self.t1.channel_up()
        self.t1.channel_up()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
        self.t1.channel_up()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    def test_channel_down(self) -> None:
        """
        Tests that the channel_down method of the Television Class works as intended
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.t1.power()
        self.t1.channel_down()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
        self.t1.channel_down()
        self.t1.channel_down()
        self.t1.channel_down()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    def test_volume_up(self) -> None:
        """
        Tests that the volume_up method of Television Class works as intended
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.t1.power()
        self.t1.volume_up()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"
        self.t1.volume_up()
        self.t1.volume_up()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"

    def test_volume_down(self) -> None:
        """
        Tests that the volume_down method of the Television Class works as intended
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        self.t1.power()
        self.t1.volume_down()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        self.t1.volume_up()
        self.t1.volume_up()
        self.t1.volume_down()
        assert self.t1.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"

    def test_str(self) -> None:
        """
        Tests the Television Object's string function, and asserts that values are as expected
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
