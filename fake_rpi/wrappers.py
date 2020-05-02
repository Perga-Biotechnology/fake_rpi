###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
# http://www.saltycrane.com/blog/2010/03/simple-python-decorator-examples/
import logging
from functools import wraps

PRINT_ON = True

logger = logging.getLogger(__name__)


def toggle_print(p):
    global PRINT_ON
    PRINT_ON = p


def printf(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        r = f(*args, **kwargs)

        if len(args):
            c = str(args[0].__class__).split('\'')[
                1]  # grab self from the class method
        else:
            c = ''  # no class

        if PRINT_ON:
            if r:
                logger.info('{}.{}{}: {}'.format(c, f.__name__, args[1:], r))
            else:
                logger.info('{}.{}{}'.format(c, f.__name__, args[1:]))
        return r
    return wrapped
