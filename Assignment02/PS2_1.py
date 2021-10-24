import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

Sig_Eqs = pd.read_csv('earthquakes-2021-10-23_17-00-59_+0800.tsv',sep='\t').iloc[1:,1:]
df_eq = Sig_Eqs.set_index('Country')
df_top10_deaths=df_eq['Total Deaths'].groupby('Country').sum().sort_values(ascending=False).head(10)

print('the top ten countries along with the total number of deaths are listed:')
for i in range(10):
    print(i+1,':',df_top10_deaths.index[i],'; the number ofdeaths:',int(df_top10_deaths.values[i]))

df_plot=Sig_Eqs[Sig_Eqs['Mag']>6.0].groupby('Year').count()['Country']
df_plot.plot(lw=0.3,ylabel='the number of eqs with larger than 6.0',figsize=(10,5))

# function returns count numbers and date by given country name
def CountEq_LargestEQ(country, df_input=Sig_Eqs):

    country=country.upper()
    count=len(Sig_Eqs[Sig_Eqs['Country']==country])

    info_list=Sig_Eqs[Sig_Eqs['Country']==country].sort_values('Mag',ascending=False).iloc[0][['Year','Mo','Dy']]

    date=str(info_list['Year'])[:-2]+'-'+str(info_list['Mo'])[:-2].zfill(2)+'-'+str(info_list['Dy']).zfill(2)

    return count, date

country_list=Sig_Eqs['Country'].unique()
arr_eqs=np.full((country_list.shape[0]-1,2),np.nan)
df_=pd.DataFrame(arr_eqs,index=country_list[0:-1],columns=['count','date of biggest'])

for country in country_list[0:-1]:
    df_.loc[country,['count','date of biggest']]=CountEq_LargestEQ(country)

df_=df_.sort_values('count',ascending=False)

# print the several head lines of result
print('The total numbers of earthquakes in each countries:\n')
print('(Taiwan province of China has not been counted)\n')
for i in range(len(df_)):
    print(int(df_.iloc[i,:]['count']),'\t',df_.index[i].title())    