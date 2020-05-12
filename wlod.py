import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

train = np.array(pd.read_csv("C:/Users/wolod/Documents/Programming/Kaggle/uncertainty/input/sales_train_validation.csv"))

plt.plot(np.arange(np.shape(train)[1] - 6), np.sum(train,axis=0)[6:])

plt.show()