import abc


class ADCReader(abc.ABC):
    def __init__(self):
        pass

    def __init__(self, *args):
        pass

    @abc.abstractmethod
    def initialize(self, *args):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass

    @abc.abstractmethod
    def read_value(self, channel: int = None, *args):
        pass

    @abc.abstractmethod
    def delay(self, delay: int = None):
        pass

    @abc.abstractmethod
    def speed(self, speed: int = None):
        pass

    @abc.abstractmethod
    def maxvalue(self):
        pass

    @abc.abstractmethod
    def minvalue(self):
        pass
