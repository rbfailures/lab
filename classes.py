class Television:
    """
    A class representing details for a Television object
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a Television object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        Method to set the status of the Television to on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self):
        """
        Method to increase the channel of Television object by increments of 1, not to increase past 3
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

    def channel_down(self):
        """
        Method to decrease the channel of Television object by increments of 1, not to decrease past 0
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self):
        """
        Method to increase the volume of Television object by 1, not to go past 2
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = self.__volume
            else:
                self.__volume += 1
        else:
            pass

    def volume_down(self):
        """
        Method to decrease the volume of Television object, not to go past 0
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = self.__volume
            else:
                self.__volume -= 1
        else:
            pass

    def __str__(self) -> String:
        """
        Method to write Television Object and its characteristics as a string
        :return: Television Object as string
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
