# Fake Raspberry Pi Interface

## Use Case

|          |                        |
| -------- | ---------------------- |
| Adafruit | LSM303(accelerometer)  |
| nxp_imu  | adafruit accelerometer |
| GPIO     | gpio pins              |
| picamera | camera                 |
| RPi      | PWM                    |
| smbus    | i2c                    |
| serial   | not done yet           |


## Development

To submit pull requests for new sensors or fixes, just do:

```
git clone https://github.com/ycbayrak/fake_rpi.git
cd fake_rpi
poetry install
```

Then do a pull request.

## Usage

To fake RPi.GPIO or smbus, this following
code must be executed before your application:

```python
# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
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

# Changelog

| Date       | Ver.  | Notes                                         |
| ---------- | ----- | --------------------------------------------- |
| 2020-04-03 | 0.7.0 | package structure changed                     |
| 2020-04-03 | 0.6.4 | additions to gpio and camera                  |
| 2020-02-03 | 0.6.3 | moved to toml and github workflows            |
| 2019-10-19 | 0.6.2 | fixes from scivision and Rotzbua              |
| 2019-03-29 | 0.6.1 | bug fix with randint range                    |
| 2017-11-30 | 0.6.0 | bug fix with printing                         |
| 2017-10-23 | 0.5.3 | bug fix with randint                          |
| 2017-09-05 | 0.5.1 | flushing out interfaces                       |
| 2017-07-07 | 0.3.0 | fixed bugs, print statement, and reduced dups |
| 2017-04-08 | 0.1.0 | initial python3 setup and support             |
| 2017-04-02 | 0.0.2 | pushed to pypi with landscape.io fixes        |
| 2017-04-01 | 0.0.1 | created                                       |
