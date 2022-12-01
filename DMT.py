import numpy as np
import matplotlib.pyplot as mpt
import pandas as pd
data_set = pd.read_csv('Dataset.csv')
x = data_set.iloc[:, :-1].values
from sklearn.impute import SimpleImputer
imputa = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputa.fit(x[:, 1:3])
x[:, 1:3] = imputa.transform(x[:, 1:3])
