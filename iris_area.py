import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np


df = pd.read_csv("Iris.csv")

species_list = list(df[:]['Species'])

id_list = df['Id'].to_list()

sepal_length_list = df["SepalLengthCm"].to_list()

sepal_width_list = df["SepalWidthCm"].to_list()

petal_length_list = df['PetalLengthCm'].to_list()

petal_width_list = df['PetalWidthCm'].to_list()

plt.fill_between(np.arange(150), sepal_length_list, color="blue",
                 alpha=0.5, label='sepal length')
plt.fill_between(np.arange(150), sepal_width_list, color="green",
                 alpha=0.5, label='sepal width')
plt.fill_between(np.arange(150), petal_length_list, color="pink",
                 alpha=0.5, label='sepal length')
plt.fill_between(np.arange(150), petal_width_list, color="yellow",
                 alpha=0.5, label='sepal width')

plt.legend()
plt.show()