import numpy as np

from .wrappers import printf
from .base import Base


class eAWBGainModes:
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


class eImageEffects:
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


class eFlashModes:
    OFF = "off"
    AUTO = "auto"
    ON = "on"
    REDEYE = "redeye"
    FILLIN = "fillin"
    TORCH = "torch"


class eExposureModes:
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


class eDRCStrengths:
    OFF = 'off'
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

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


class PiCamera(Base):
    """Fake camera class"""

    AWB_MODES = eAWBGainModes()
    EXPOSURE_MODES = eExposureModes()
    DRC_STRENGTHS= eDRCStrengths()
    FLASH_MODES = eFlashModes()
    IMAGE_EFFECTS = eImageEffects()
    
    resolution = (1280, 720)
    awb_gains = 0.0
    awb_mode = AWB_MODES.AUTO
    drc_strength = DRC_STRENGTHS.OFF
    exposure_mode = EXPOSURE_MODES.AUTO
    flash_mode = FLASH_MODES.OFF
    image_effect = IMAGE_EFFECTS.NONE
    brightness = 50
    contrast = 0
    iso = 0
    sharpness = 0

    def __init__(self):
        Base.__init__(self, self.__class__)
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def close(self):
        pass

    @printf
    def capture(output, format=None, use_video_port=False, resize=None, splitter_port=0, bayer=False, **options):
        pass

    @printf
    def capture_continuous(output, format=None, use_video_port=False, resize=None, splitter_port=0, burst=False, bayer=False, **options):
        pass

    @printf
    def capture_sequence(outputs, format='jpeg', use_video_port=False, resize=None, splitter_port=0, burst=False, bayer=False, **options):
        pass

class array(object):
    """Fake class"""

    @staticmethod
    def PiRGBArray(cam, size):
        return BGR(size)
