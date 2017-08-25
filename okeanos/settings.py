################################################################################
#   Import extra settings
################################################################################

from settings_dev import *

try:
    from settings_local import *
except ImportError:
    pass
