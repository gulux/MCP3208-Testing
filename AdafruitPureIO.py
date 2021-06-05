import Adafruit_PureIO.spi as  SPI

from ADCReader import ADCReader


class AdaPIO(ADCReader):  # SPI driver
    _spi = None
    _delay = 0
    _MAX_SPEED = 1000000

    def initialize(self):
        self._spi = SPI.SPI((0, 0), self._MAX_SPEED, 8)

    def initialize(self, speed: int = 2000000, delay: int = 0):
        self._delay = delay
        self._spi = SPI.SPI((0, 0), speed, 8)

    def __read(self, channel: int = 0, differential: bool = False) -> int:
        """Read data from MCP3208 Chip via SPI in a transfer."""
        adc: int = -1
        data_in = None

        if differential:
            data_in = [4 | (channel & 4) >> 2, (channel & 3) << 6, 0]
        else:
            data_in = [6 | (channel & 4) >> 2, (channel & 3) << 6, 0]

        adc = self._spi.transfer(data_in, delay=self._delay)
        data = ((adc[1] & 15) << 8) + adc[2]
        return int(data)

    def cleanup(self):
        self._spi = None

    def read_value(self, channel: int = 0, differential: bool = False):
        if channel < 0 or channel > 7 or self._spi is None:
            raise Exception('wrong channel')
        return self.__read(channel, differential)

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value: int):
        self._delay = value

    @property
    def speed(self):
        return self._spi.max_speed_hz

    @speed.setter
    def speed(self, value: int):
        self._spi.max_speed_hz = value

    @property
    def maxvalue(self):
        return 4095

    @property
    def minvalue(self):
        return 0
