#!/usr/bin/python3
# --------------------------------------

import spidev


def main():
    # Open SPI bus
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 100000

    # Function to read SPI data from MCP3208 chip
    # Channel must be an integer 0-7
    def ReadChannel(channel):
        adc = spi.xfer([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])
        data = ((adc[1] & 15) << 8) + adc[2]
        return data

    for i in range(0, 10):
        print(ReadChannel(0))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
