# Fake Raspberry Pi Interface

[![GitHub version](https://img.shields.io/github/v/release/ycbayrak/fake_rpi.svg)](https://github.com/ycbayrak/fake_rpi)
[![Build Status](https://travis-ci.org/ycbayrak/fake_rpi.svg?branch=master)](https://travis-ci.org/ycbayrak/fake_rpi)
[![GitHub issues](https://img.shields.io/github/issues/ycbayrak/fake_rpi)](https://GitHub.com/ycbayrak/fake_rpi/issues/)


## Use Case

I do a lot of development on my Powerbook and I got tired of constantly
creating a fake interface for dev on my laptop and testing on Travis CI.

So, does this simulate everything on a Raspberry Pi? **No!** 

|          |                       |
| -------- | --------------------- |
| Adafruit | LSM303(accelerometer) |
| GPIO     | gpio pins             |
| picamera | camera                |
| RPi      | PWM                   |
| smbus    | i2c                   |
| serial   | not done yet          |


## Development

To submit pull requests and do development:

```
git clone https://github.com/ycbayrak/fake_rpi.git
cd fake_rpi
poetry install
```

## Usage

To fake RPi.GPIO or smbus, this following
code must be executed before your application:

```python
# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)
```

Then you can keep your usual imports in your application:

```python
import RPi.GPIO as GPIO
import smbus

GPIO.setmode(io.BCM) # now use the fake GPIO
b = GPIO.input(21)

sm = smbus.SMBus(1) # now use the fake smbus
b = sm.read_byte_data(0x21, 0x32)  # read in a byte
```

Turning on/off fake calls logging:

```python
from fake_rpi import toggle_print

# by default it prints everything to std.error
toggle_print(False)  # turn on/off printing
```

But I need `smbus` to return a specific byte for unit testing! Ok, then
create a child of my `smbus` like below and modify *only* the methods
you need changed:

```python
from fake_rpi import smbus
from fake_rpi import printf

class MyBus(smbus.SMBus):
    @printf
    def read_byte_data(self, i2c_addr, register):
        ret = 0xff
        if i2c_addr == 0x21:
            ret = 0x55
        elif i2c_addr == 0x25:
            ret = 0x11
        return ret

sm = MyBus()
b = sm.read_byte_data(0x21, 0x32)  # read in a byte
```

### Printing On or Off

Here is the output from `example.py` in the `git` repo when the printing
is toggled on or off:

```
$ ./example.py
<<< WARNING: using fake raspberry pi interfaces >>>

$ ./example.py
<<< WARNING: using fake raspberry pi interfaces >>>
fake_rpi.RPi.PWM.__init__()
fake_rpi.RPi.PWM.start(5,)
fake_rpi.smbus.SMBus.__init__(1,)
fake_rpi.smbus.SMBus.write_byte_data(1, 2, 3)
fake_rpi.smbus.SMBus.read_byte_data(1, 2): 21
fake_rpi.smbus.SMBus.close()
__main__.MyBus.__init__()
__main__.MyBus.read_byte_data(1, 2): 72
__main__.MyBus.read_i2c_block_data(1, 2, 3): [90, 90, 90]
```

