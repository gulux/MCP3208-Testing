import spidev

from ADCReader import ADCReader


class SPIADC(ADCReader):  # SPI driver
    _spi = spidev.SpiDev()
    _delay_usec = 0
    _max_speed = 2000000
    _apply = False

    def __read(self, channel: int = 0, differential: bool = False) -> int:
        """Read data from MCP3208 Chip via SPI."""
        adc: int = -1
        if not differential:
            adc = self._spi.xfer([6 | (channel & 4) >> 2, (channel & 3) << 6, 0], self._max_speed, self._delay_usec)
        else:
            adc = self._spi.xfer([4 | (channel & 4) >> 2, (channel & 3) << 6, 0], self._max_speed, self._delay_usec)
        data = ((adc[1] & 15) << 8) + adc[2]
        return int(data)

    def initialize(self):
        self._spi.open(0, 0)
        self._spi.max_speed_hz = self._max_speed

    def initialize(self, speed: int = 2000000, delay: int = 0):
        self._spi.open(0, 0)
        self._max_speed = speed
        self._spi.max_speed_hz = self._max_speed
        self._delay_usec = delay

    def cleanup(self):
        self._spi.close()

    def read_value(self, channel: int = 0, differential: bool = False):
        if channel < 0 or channel > 7:
            raise Exception('wrong channel')
        return self.__read(channel, differential)

    @property
    def delay(self):
        return self._delay_usec

    @delay.setter
    def delay(self, value: int):
        self._delay_usec = value

    @property
    def speed(self):
        return self._max_speed

    @speed.setter
    def speed(self, value: int):
        self._max_speed = value
        self._spi.max_speed_hz = value

    @property
    def maxvalue(self):
        return 4095

    @property
    def minvalue(self):
        return 0
