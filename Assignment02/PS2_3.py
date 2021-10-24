import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy.stats.mstats import theilslopes
from scipy.stats import kendalltau

df_3sites=pd.read_csv('data/data_3stations.csv')
df_3sites=df_3sites.set_index('time')
df_3sites.index=pd.to_datetime(df_3sites.index)

df_annual=df_3sites['huaxian'].resample('y').mean()
df_annual.plot(xlabel='Date',ylabel='Discharge of Huaxian',figsize=(9,5))

def linear_statistic(dat):
    dat0 = np.arange(len(dat))
    dat1 = dat0.copy()

    iddat1 = np.isfinite(dat)
    degree = 1
    x = dat1[iddat1]
    y = dat[iddat1]
    fit = np.polyfit(x, y, degree)
    model = np.poly1d(fit)
    df = pd.DataFrame(columns=['y', 'x'])
    df['x'] = x
    df['y'] = y
    results = smf.ols(formula='y ~ model(x)', data=df).fit()
    slope = fit[0]
    p_value = results.f_pvalue
    fit_fn = np.poly1d(fit)

    # changes, mean of data, trend in percentage, p-value
    return slope * len(dat), np.nanmean(dat), (slope * len(dat)) / np.nanmean(dat) * 100, p_value, fit_fn

change_value,mean_value,change_ratio, significance, linear_fit_params =linear_statistic(df_3sites['huaxian'].resample('y').mean().values)

print('the change value of the data is',change_value.round(2),'mm/yr')
print('the mean value of the data is',mean_value.round(2),'mm/yr')
print('the change ratio of the data is',change_ratio.round(2),'%')
print('the significance of MK test is',significance.round(6),)
print('the linear fit parameters are',linear_fit_params)