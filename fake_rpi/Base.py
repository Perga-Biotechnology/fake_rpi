###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
import logging

logger = logging.getLogger(__name__)

class Base(object):
    def __init__(self, name=None):
        logger.info('[fake_rpi] Using fake raspberry pi interfaces')
        if name:
            logger.info('[fake_rpi] Using: {}'.format(name))
