import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

df_input=pd.read_csv('data/2281305.csv',low_memory=False)
df_windspeed=pd.DataFrame(np.full((len(df_input),1),np.nan),index=df_input['DATE'],columns=['speed rate'])
for i in range(len(df_windspeed)):
    df_windspeed.iloc[i,0]=int(df_input['WND'][i][8:12])
#    if(i%10000==0):
#        print(i,'/',len(df_windspeed),'...')

arr_wind=df_windspeed['speed rate'].values
arr_wind[arr_wind==9999]=np.nan
df_windspeed['speed rate']=arr_wind

df_windspeed.index=pd.to_datetime(df_windspeed.index)
df_monthly=df_windspeed.resample('m').mean()

def plot_timeperiod(start,end,data=df_monthly):
    time=pd.date_range(start=start,end=end,freq='m')
    df_data=pd.DataFrame(index=time,columns=['wind speed'])
    s=(int(start[0:4])-2010)*12+int(start[5:7])-1
    e=(int(end[0:4])-2010)*12+int(end[5:7])-1
    n=e-s
    for i in range(n):
        df_data.iloc[i,0]=data.iloc[s+i,0]/10
    df_data.plot(ylabel='wind speed (m/s)',figsize=(8,5))

plot_timeperiod('2010-01','2020-10')   