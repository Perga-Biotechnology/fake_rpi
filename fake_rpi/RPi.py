from fake_rpi.wrappers import printf
from fake_rpi.base import Base
from random import randint


class _GPIO(Base):

    class PWM(Base):
        @printf
        def __init__(self, channel=0, frequency=0):
            Base.__init__(self, self.__class__)

        @printf
        def start(self, dc):
            pass

        def stop(self):
            pass

        def ChangeDutyCycle(self, dc):
            pass

        def ChangeFrequency(self, frequency):
            pass

    # Values
    LOW = 0
    HIGH = 1

    # Modes
    BCM = 11
    BOARD = 10

    # Pull
    PUD_OFF = 20
    PUD_DOWN = 21
    PUD_UP = 22

    # Edges
    RISING = 31
    FALLING = 32
    BOTH = 33

    # Functions
    OUT = 0
    IN = 1
    SERIAL = 40
    SPI = 41
    I2C = 42
    HARD_PWM = 43
    UNKNOWN = -1

    # Versioning
    RPI_REVISION = 2
    VERSION = '0.5.6'

    def __init__(self):
        Base.__init__(self, self.__class__)
        self._inputs = [None] * 40  # We have 40 input pins

    @printf
    def setwarnings(self, a): pass

    @printf
    def setmode(self, a): pass

    @printf
    def getmode(self): return GPIO.BCM

    @printf
    def setup(self, channel, state, initial=0, pull_up_down=None): pass

    @printf
    def input(self, channel):
        if self._inputs[channel] is not None:
            return self._inputs[channel]
        return randint(0, 1)

    @printf
    def set_input(self, channel, value):
        self._inputs[channel] = value

    @printf
    def cleanup(self, a=None): pass

    @printf
    def output(self, channel, state): pass

    @printf
    def wait_for_edge(self, channel, edge): pass

    @printf
    def add_event_detect(self, channel, edge,
                         callback=None, bouncetime=None): pass

    @printf
    def add_event_callback(self, channel, callback=None): pass

    @printf
    def remove_event_detect(self, channel): pass

    @printf
    def event_detected(self, channel): return False

    @printf
    def gpio_function(self, channel): return GPIO.OUT


GPIO = _GPIO()
