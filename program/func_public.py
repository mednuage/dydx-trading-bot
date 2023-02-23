# Fonctions traitant les données publiques de DyDX
from constants import RESOLUTION
from func_utils import get_ISO_times
import pandas as pd
import numpy as np
import time
from pprint import pprint

# Get relevant time periods for ISO from and to
ISO_TIMES = get_ISO_times()
pprint(ISO_TIMES)

# Constract Market Prices

def constract_market_prices(client):
    pass 