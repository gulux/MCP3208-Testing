from time import sleep

from ADCReader import ADCReader


class DummyADC(ADCReader):

    def initialize(self, *args):
        pass

    def cleanup(self):
        pass

    def read_value(self, channel: int = None, *args) -> int:
        return 1234

    def delay(self, delay: int = None):
        pass

    def speed(self, speed: int = None):
        pass

    def maxvalue(self):
        pass

    def minvalue(self):
        pass
