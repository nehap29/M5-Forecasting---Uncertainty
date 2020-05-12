import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

train = np.array(pd.read_csv("input/m5-forecasting-uncertainty/sales_train_validation.csv"))
sell_prices = pd.read_csv("input/m5-forecasting-uncertainty/sell_prices.csv")
print(train[2])

plt.plot(np.arange(np.shape(train)[1] - 6), np.cumsum(np.sum(train,axis=0)[6:]))

plt.show()