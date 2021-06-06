# MCP3208-Testing
Python module for testing parameters with different libraries 

Install spidev (https://pypi.org/project/spidev/): *pip3 install spidev*

Install AdaFruit-PureIO (https://pypi.org/project/Adafruit-PureIO/): *pip3 install AdaFruit-PureIO*

Wiring schemas for simple (https://oshwlab.com/gulux/simple-mcp3208) and parameter testing (https://oshwlab.com/gulux/mcp3208-params).

Run *python3 SimpleMCP3208.py* or *python3 main.py*

Edit main.py to investigate effects of different parameters in spi communication, e.g. speed, differential, delay.
Also change lib for spi communication.

