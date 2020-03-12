#https://github.com/flyte/pcf8574
pip install smbus-cffi
apt-get install libffi-dev
pip install pcf8574

#https://www.brainy-bits.com/i2c-explained-i2c-keypad/
#https://www.waveshare.com/wiki/Raspberry_Pi_Tutorial_Series:_I2C
#https://custom-build-robots.com/electronic/raspberry-pi-8-bit-io-port-expander-pcf8574/8823?lang=en
from pcf8574 import PCF8574

i2c_port_num = 1

pcf_address = 0x20

pcf = PCF8574(i2c_port_num, pcf_address)

pcf.port
#[True, True, True, True, True, True, True, True]

pcf.port[0] = False
#[False, True, True, True, True, True, True, True]

pcf.port = [True, False, True, False, True, False, True, False]

pcf.port[7]




