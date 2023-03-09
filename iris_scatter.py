import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Iris.csv")

sepal_length_list = df["SepalLengthCm"].to_list()
print(sepal_length_list)

sepal_width_list = df["SepalWidthCm"].to_list()

plt.scatter(sepal_length_list, sepal_width_list, color = 'green')

plt.show()
