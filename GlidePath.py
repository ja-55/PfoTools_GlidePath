# IMPORTS
import pandas as pd
import numpy as np
import datetime as dt

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# SET SEED FOR REPEATABILITY
np.random.seed(0)

# ASSUMPTIONS: BALANCES
bal_init = 500
contrib = 100
rtn_mu = 0.07
rtn_sgma = 0.12

# ASSUMPTIONS: DATES
yrs = 25
beg_dt = dt.date(2022,1,1)
end_dt = beg_dt + dt.timedelta(years = yrs)
end_dt_plot = end_dt + dt.timedelta(months = 1)
dt_yr5 = beg_dt + dt.timedelta(years = 5)
dt_yr10 = beg_dt + dt.timedelta(years = 10)
dt_yr20 = beg_dt + dt.timedelta(years = 20)
frq = 'MS'
pds = (end_dt.year - beg_dt.year) * 12 + (end_dt.month - beg_dt.month) + 1
dates = pd.date_range(start = beg_dt, freq = frq, end = end_dt)

# ASSUMPTIONS: OTHER
sims = 101
cols = ['BB','Con_Base','Con_Inc','Con_Oth','Returns','EB']
plt_lgnd = ['Median','10th Percentile','90th Percentile']

# EMPTY DATAFRAMES
eb_df = pd.DataFrame(index = dates)
stat_df = pd.DataFrame(index = dates)
