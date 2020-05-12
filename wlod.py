import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

train = np.array(pd.read_csv("../m5-forecasting-uncertainty/sales_train_validation.csv"))
sell_prices = pd.read_csv("../m5-forecasting-uncertainty/sell_prices.csv")
print(train[2])

for i in range(1,int(np.shape(train)/2)):
    plt.plot(np.arange(np.shape(train)[1] - 6), np.cumsum(train[i][6:]))

plt.show()