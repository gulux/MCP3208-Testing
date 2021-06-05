import array
import time

from statistics import median, mean, stdev
from typing import List

from AdafruitPureIO import AdaPIO
from SPIADC import SPIADC
from DummyADC import DummyADC


def test_params(reader, samples, channels, speeds, delays, differential):
    print(f' speed | delay | ch. | #meas. |  min  |  max  |  mean  | stdev | median | time ')
    for s in speeds:
        for d in delays:
            reader.initialize(s, d)
            for channel in channels:
                # start measurement
                values = array.array('H', list(range(samples)))

                start_time: float = time.time()
                for i in range(0, samples):
                    values[i] = (reader.read_value(channel, differential))

                time_diff: float = time.time() - start_time

                print(f'{s:7}|{d:7}|{channel:5}|{samples:8}|'
                      f'{min(values):7}|{max(values):7}|'
                      f'{mean(values):8.2f}|{stdev(values):7.2f}|'
                      f'{median(values):8}|{time_diff:6.3f}')

            reader.cleanup()


if __name__ == '__main__':
    try:
        # test DummyADC (for development)
        # test_params(DummyADC(), 1000, [6], [5000000, 2000000, 1000000, 500000, 200000, 100000, 50000, 10000], [0], False)
        # test AdaPIO
        # test_params(AdaPIO(), 1000, [0], [5000000, 2000000, 1000000, 500000, 200000, 100000, 50000, 10000], [0], False)
        # test SPIADC with channels 4 + 6
        test_params(SPIADC(), 1000, [4, 6], [5000000, 2000000, 1000000, 500000, 200000, 100000, 50000, 10000], [0],
                    False)
    except KeyboardInterrupt:
        pass
