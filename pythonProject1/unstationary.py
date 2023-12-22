import numpy as np
# import statsmodels.api as sm

coeff = []
ss = []
for i in range(1000):
    x0 = 1
    a = np.ones(100)
    for t in range(100):
        rands = np.random.rand(100).cumsum()
        a += rands
        y = a[1:]
        x = a[:-1]
        coeffs = np.polyfit(x, y, deg=1)
        coeff.append(coeffs[0])
        res = y- coeffs[0] * x - coeffs[1]
        r = sm.tsa.adfuller(res)
        ss.append(r)

print(r)