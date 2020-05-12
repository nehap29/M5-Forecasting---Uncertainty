import pandas as pd     
import matplotlib.pyplot as plt          # plotting
import numpy as np                       # dense matrices
from scipy.sparse import csr_matrix      # sparse matrices


train = pd.read_csv("input/m5-forecasting-uncertainty/sales_train_validation.csv")
print(train.head())

train.shape


calendar = pd.read_csv("input/m5-forecasting-uncertainty/calendar.csv")
calendar.head()