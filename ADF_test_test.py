import matplotlib.pyplot as plt
import numpy as np

#%% with [-lags:]
def generate_ar_process(lags, coefs,length):

    #cast coefs to np array
    coefs = np.array(coefs)

    #initial values
    series = [np.random.normal() for _ in range(lags)]

    for _ in range(length):
        #get previous values of the series, reversed
        prev_vals = series[-lags:][::-1]

        #get new value of time series
        new_val = np.sum(np.array(prev_vals) * coefs) + np.random.normal()

        series.append(new_val)

    return np.array(series)
#%%AR(1) Process

#Stationary

ar_1_process = generate_ar_process(2, [.5, .2], 100)
plt.figure(figsize=(10,4))
plt.plot(ar_1_process)
plt.title('Stationary AR(1) Process', fontsize=18)
plt.show()

#%% without [-lags:]
def generate_ar_process(lags, coefs,length):

    #cast coefs to np array
    coefs = np.array(coefs)

    #initial values
    series = [np.random.normal() for _ in range(lags)]

    for _ in range(length):
        #get previous values of the series, reversed
        prev_vals = series[::-1]

        #get new value of time series
        new_val = np.sum(np.array(prev_vals) * coefs) + np.random.normal()

        series.append(new_val)

    return np.array(series)
#%%AR(1) Process

#Stationary

ar_1_process = generate_ar_process(2, [.6, .3], 100)
plt.figure(figsize=(10,4))
plt.plot(ar_1_process)
plt.title('Stationary AR(1) Process', fontsize=18)
plt.show()

#%%
a = np.arange(1, 16).reshape([3, 5])
print(a, type(a))
print (a.shape, a.ndim)
b = np.array([2, 3, 4, 5, 6])
print(b)
print(b.shape, b.ndim)
print(a*b)


