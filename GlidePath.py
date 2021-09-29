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
cols = ['BB','Contrib','Returns','EB']
plt_lgnd = ['Median','10th Percentile','90th Percentile']

# EMPTY DATAFRAMES
eb_df = pd.DataFrame(index = dates)
stat_df = pd.DataFrame(index = dates)



# FILL DATAFRAMES

for sim in range(sims):
    
    temp_df = pd.DataFrame(columns = cols, index = dates)
    exp_ret = pd.DataFrame(np.random.normal(rtn_mu, rtn_sgma, pds), index = dates)
    
    for index, row in temp_df.iterrows():
        if index == beg_date:
            row['BB'] = 0
            row['Contrib'] = bal_init + contrib
            row['Returns'] = (row['BB'] + row['Contrib'] / 2) * (exp_ret.loc[index,:].values[0] / 12)
            row['EB'] = (row['BB'] + row['Contrib'] + row['Returns'])
        else:
            row['BB'] = temp_df.shift(1).loc[index,'EB']
            row['Contrib'] = contrib
            row['Returns'] = (row['BB'] + row['Contrib'] / 2) * (exp_ret.loc[index,:].values[0] / 12)
            row['EB'] = (row['BB'] + row['Contrib'] + row['Returns'])
    eb_df.loc[:,sim] = temp_df['EB']

# FIND MEDIAN, 90TH PERCENTILE, AND 10TH PERCENTILE
col_med = eb_df.loc[end_dt,:].loc[eb_df.loc[end_dt,:] == eb_df.loc[end_dt,:].median()].index[0]
col_90p = eb_df.loc[end_dt,:].loc[eb_df.loc[end_dt,:] == eb_df.loc[end_dt,:].quantile(q = 0.9)].index[0]
col_10p = eb_df.loc[end_dt,:].loc[eb_df.loc[end_dt,:] == eb_df.loc[end_dt,:].quantile(q = 0.1)].index[0]

# STORE MEDIAN, 90TH PERCENTILE, AND 10TH PERCENTILE IN DATAFRAME
stat_df = eb_df.loc[:,[col_med, col_90p, col_10p]]

# PLOT GLIDEPATH
plt.close()
fig, ax = plt.subplots(1,1, figsize = (15,7))
stat_df.plot.line(ax = ax, legend = True).legend(plt_lgnd, fontsize = 14)
plt.scatter([dt_24] * 3, stat_df.loc[dt_24,:].values, marker = 'o', c = 'red', s = 50)
plt.scatter([dt_26] * 3, stat_df.loc[dt_26,:].values, marker = 'o', c = 'blue', s = 50)
plt.scatter([end_dt] * 3, stat_df.loc[end_dt,:].values, marker = 'o', c = 'black', s = 50)
plt.title('Figure 1:Projected Portfolio Balance', fontweight = 'bold', fontsize = 15)
plt.ylabel('Projected Wealth ($)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
ax.set_xlim([beg_dt, end_dt_plt])

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
plt.gca().yaxis.set_major_formatter(tick)

# DISPLAY BALANCES AS OF KEY DATES
print(stat_df.loc[[dt_yr5,dt_yr10,dt_yr20],:])
