import logging

logger = logging.getLogger(__name__)

class Base(object):
    def __init__(self, name=None):
        logger.info('[fake_rpi] Using fake raspberry pi interfaces')
        if name:
            logger.info('[fake_rpi] Using: {}'.format(name))
