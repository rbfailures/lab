import pytest
from classes import *


class Test:
    def setup_method(self) -> None:
        """
        Setup method for testing
        :return: None
        """
        self.t1 = Television()

        self.t2 = Television()
        self.t2.power()
        self.t2.volume_up()
        self.t2.channel_up()

        self.t3 = Television()
        self.t3.volume_up()
        self.t3.channel_up()

        self.t4 = Television()
        self.t4.power()
        self.t4.volume_up()
        self.t4.volume_up()
        self.t4.volume_up()
        self.t4.channel_up()
        self.t4.channel_up()
        self.t4.channel_up()
        self.t4.channel_up()

        self.t5 = Television()
        self.t5.power()
        self.t5.volume_down()
        self.t5.channel_down()

    def teardown_method(self) -> None:
        """
        Teardown method for testing
        :return: None
        """
        del self.t1
        del self.t2
        del self.t3
        del self.t4
        del self.t5

    def test_init(self) -> None:
        """
        Tests if the __init__ function of class Television initializes object with correct values
        :return: None
        """
        assert self.t1.get_status() is False
        assert self.t1.get_channel() == 0
        assert self.t1.get_volume() == 0

    def test_get_status(self) -> None:
        """
        Tests if the get_status method of the Television Class works as intended
        :return: None
        """
        assert type(self.t1.get_status()) is bool
        assert self.t1.get_status() is False

        assert self.t2.get_status() is True

        assert self.t3.get_status() is False

    def test_get_volume(self) -> None:
        """
        Tests if the get_volume method of Television Class works as intended
        :return: None
        """
        assert type(self.t1.get_volume()) is int
        assert self.t1.get_volume() == 0

        assert self.t2.get_volume() == 1

        assert self.t3.get_volume() == 0

        assert self.t4.get_volume() == 2

        assert self.t5.get_volume() == 0

    def test_get_channel(self) -> None:
        """
        Tests if the get_channel method of Television Class works as intended
        :return: None
        """
        assert type(self.t1.get_channel()) is int
        assert self.t1.get_channel() == 0

        assert self.t2.get_channel() == 1

        assert self.t3.get_channel() == 0

        assert self.t4.get_channel() == 0

        assert self.t5.get_channel() == 3

    def test_power(self) -> None:
        """
        Tests that the power method of Television Class works as intended
        :return: None
        """
        self.t1.power()
        assert self.t1.get_status() is True

        self.t2.power()
        assert self.t2.get_status() is False

        self.t3.power()
        assert self.t3.get_status() is True

        self.t4.power()
        assert self.t4.get_status() is False

        self.t5.power()
        assert self.t5.get_status() is False

    def test_channel_up(self) -> None:
        """
        Tests that the channel_up method of Television Class works as intended
        :return: None
        """
        self.t1.channel_up()
        assert self.t1.get_channel() == 0

        self.t2.channel_up()
        assert self.t2.get_channel() == 2

        self.t3.channel_up()
        assert self.t3.get_channel() == 0

        self.t4.channel_up()
        assert self.t4.get_channel() == 1

        self.t5.channel_up()
        assert self.t5.get_channel() == 0

    def test_channel_down(self) -> None:
        """
        Tests that the channel_down method of the Television Class works as intended
        :return: None
        """
        self.t1.channel_down()
        assert self.t1.get_channel() == 0

        self.t2.channel_down()
        assert self.t2.get_channel() == 0

        self.t3.channel_down()
        assert self.t3.get_channel() == 0

        self.t4.channel_down()
        assert self.t4.get_channel() == 3

        self.t5.channel_down()
        assert self.t5.get_channel() == 2

    def test_volume_up(self) -> None:
        """
        Tests that the volume_up method of Television Class works as intended
        :return: None
        """
        self.t1.volume_up()
        assert self.t1.get_volume() == 0

        self.t2.volume_up()
        assert self.t2.get_volume() == 2

        self.t3.volume_up()
        assert self.t3.get_volume() == 0

        self.t4.volume_up()
        assert self.t4.get_volume() == 2

        self.t5.volume_up()
        assert self.t5.get_volume() == 1

    def test_volume_down(self) -> None:
        """
        Tests that the volume_down method of the Television Class works as intended
        :return: None
        """
        self.t1.volume_down()
        assert self.t1.get_volume() == 0

        self.t2.volume_down()
        assert self.t2.get_volume() == 0

        self.t3.volume_down()
        assert self.t3.get_volume() == 0

        self.t4.volume_down()
        assert self.t4.get_volume() == 1

        self.t5.volume_down()
        assert self.t5.get_volume() == 0

    def test_str(self) -> None:
        """
        Tests the Television Object's string function, and asserts that values are as expected
        :return: None
        """
        assert self.t1.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.t2.__str__() == "TV status: Is on = True, Channel = 1, Volume = 1"
        assert self.t3.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"
        assert self.t4.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"
        assert self.t5.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"
