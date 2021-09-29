# IMPORTS
import pandas as pd
import numpy as np
import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# SET SEED FOR REPEATABILITY
np.random.seed(0)

# ASSUMPTIONS
bal_init = 500
contrib = 100
rtn_mu = 0.07
rtn_sgma = 0.12
