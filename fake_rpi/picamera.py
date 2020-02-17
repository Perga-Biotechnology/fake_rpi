###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
import numpy as np  # type: ignore
# import platform
from .wrappers import printf
from .Base import Base


class AWBGainModes:
    OFF = "off"
    AUTO = "auto"
    SUNLIGHT = "sunlight"
    CLOUDY = "cloudy"
    SHADE = "shade"
    TUNGSTEN = "tungsten"
    FLUORESCENT = "fluorescent"
    INCANDESCENT = "incandescent"
    FLASH = "flash"
    HORIZON = "horizon"


class ImageEffects:
    NONE = "none"
    NEGATIVE = "negative"
    SOLARIZE = "solarize"
    SKETCH = "sketch"
    DENOISE = "denoise"
    EMBOSS = "emboss"
    OILPAINT = "oilpaint"
    HATCH = "hatch"
    GPEN = "gpen"
    PASTEL = "pastel"
    WATERCOLOR = "watercolor"
    FILM = "film"
    BLUR = "blur"
    SATURATION = "saturation"
    COLORSWAP = "colorswap"
    WASHEDOUT = "washedout"
    POSTERISE = "posterise"
    COLORPOINT = "colorpoint"
    COLORBALANCE = "colorbalance"
    CARTOON = "cartoon"
    DEINTERLACE1 = "deinterlace1"
    DEINTERLACE2 = "deinterlace2"


class FlashModes:
    OFF = "off"
    AUTO = "auto"
    ON = "on"
    REDEYE = "redeye"
    FILLIN = "fillin"
    TORCH = "torch"


class ExposureModes:
    OFF = "off"
    AUTO = "auto"
    NIGHT = "night"
    NIGHT_PREVIEW = "nightpreview"
    BACKLIGHT = "backlight"
    SPOTLIGHT = "spotlight"
    SPORTS = "sports"
    SNOW = "snow"
    BEACH = "beach"
    VERYLONG = "verylong"
    FIXEDFPS = "fixedfps"
    ANTISHAKE = "antishake"
    FIREWORKS = "fireworks"



class BGR(object):
    """Fake class"""

    @printf
    def __init__(self, sz):
        # constructor
        self.array = np.random.rand(*sz)

    @printf
    def truncate(self, num):
        # refreshes the fake image
        self.array = np.random.rand(*self.array.shape)


# class picamera(object):
#     """Fake class"""
class PiCamera(Base):
    """Fake class"""

    AWB_MODES = (
        'off',
        'auto',
        'sunlight',
        'cloudy',
        'shade',
        'tungsten',
        'fluorescent',
        'incandescent',
        'flash',
        'horizon'
    )
    EXPOSURE_MODES = (
        'off',
        'auto',
        'night',
        'nightpreview',
        'backlight',
        'spotlight',
        'sports',
        'snow',
        'beach',
        'verylong',
        'fixedfps',
        'antishake',
        'fireworks'
    )
    DRC_STRENGTHS= (
        'off',
        'low',
        'medium',
        'high'
    )
    FLASH_MODES = (
        'off',
        'auto',
        'on',
        'redeye',
        'fillin',
        'torch'
    )

    IMAGE_EFFECTS = (
        'none',
        'negative',
        'solarize',
        'sketch',
        'denoise',
        'emboss',
        'oilpaint',
        'hatch',
        'gpen',
        'pastel',
        'watercolor',
        'film',
        'blur',
        'saturation',
        'colorswap',
        'washedout',
        'posterise',
        'colorpoint',
        'colorbalance',
        'cartoon',
        'deinterlace1',
        'deinterlace2'
    )
    
    resolution = (0, 0)

    awb_gains = 0.0
    awb_mode = "auto"


    exposure_mode = "auto"
    
    brightness = 50
    contrast = 0
    iso = 0
    sharpness = 0

    flash_mode = "off"
    image_effect = "none"

    def __init__(self):
        # empty constructor
        # print('WARNING: Fake_RPi PiCamera on {}'.format(platform.system().lower()))
        Base.__init__(self, self.__class__)
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def close(self):
        # this does nothing
        pass

    @printf
    def capture(self, image, format, use_video_port):
        # this does nothing
        pass


class array(object):
    """Fake class"""

    @staticmethod
    def PiRGBArray(cam, size):
        return BGR(size)
