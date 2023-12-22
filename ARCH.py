import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA #tsa=time series analysis
import arch
import re

#%% import the data and change the type

df = pd.read_csv('SSE_2014-2015.csv') # only input the file's name
change = df['change'].str.strip('%') # select a subset of a dataframe and remove the '%' sign
print(type(change))
# change=change.to_string() #convert the series into string
# change=change.replace(" ","") #remove the space in the string
# change=change.replace("\n","") # remove the newline character
# change=change.splitlines() #convert the string into list
# change=re.sub(r'\n\d?\d?\d?', '', change) #remove the newline character and the trailing numbers, one \d? for one digit
# change=change[1:]
print(change[0:10])
change=pd.to_numeric(change, errors='coerce') #convert the object into float, but the percentage number can't be recognized
change = change/100
print(change[0:10])

#%% draw the data and the mean

plt.figure(figsize=(15,5))
plt.plot(range(len(change)), change)
change.rolling(12).mean().plot()
plt.show()

#%% check the stationarity by adf test

t = sm.tsa.stattools.adfuller(change)
print(t) # why the result of adf test is so messy
print("p-value: ",t[1])

#%% check the acf and pacf

fig = plt.figure(figsize=(20,5))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(change,lags = 20, ax=ax1)
ax2=fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(change,lags = 20, ax=ax2)
# why are we just looking at ar not ma, why is the lag not 4?
plt.show()

#%% build the model and see the pareameters

model = ARIMA(change, order = (4, 0, 4)).fit()
print(model.params)
plt.plot(model.predict())
plt.show()

#%% draw the residual and residuak square to see if the ARCH effect exists

at = change - model.fittedvalues
at2 = np.square(at)
plt.figure(figsize=(10,6))
plt.subplot(211)
plt.plot(at,label = 'at')
plt.legend()
plt.subplot(212)
plt.plot(at2,label='at^2')
plt.legend(loc=0)
plt.show()

#%% run the Ljung-Box test of at2

m = 25 # test for 25 acf
acf,q,p = sm.tsa.acf(at2,nlags=m,qstat=True) # return acf and p-value
out = np.c_[range(1,26),acf[1:],q,p]
output = pd.DataFrame(out, columns=['lag', "AC", "Q", "P-value"])
output = output.set_index('lag')
output

#%% deciding the order of at2 by pacf

fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(111)
fig = sm.graphics.tsa.plot_pacf(at2,lags = 30,ax=ax1)
plt.show()

#%%

train = change[:-10]
test = change[-10:]
am = arch.arch_model(train,mean='AR',lags=8,vol='ARCH',p=4)
result = am.fit()

#%%

result.summary
#%%
result.params
#%%
result.hedgehog_plot()
plt.show()

#%%

result.plot()
change.plot()
print(len(train))
# plt.savefig("figtest.jpg")
plt.show()

#%%

pre = result.forecast(horizon=10,start=478).mean
print(pre)
prediction=pd.DataFrame(pre)
plt.plot(pre.iloc[-1])
plt.show()

#%%
plt.figure(figsize=(10,4))
plt.plot(test[-10:],label='realValue')
zero=pd.DataFrame(np.zeros(489))
plt.plot(zero[-10:],label='zero')
plt.legend(loc=0)
plt.show()