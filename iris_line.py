import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Iris.csv")

id_list = df['Id'].to_list()

sepal_length_list = df["SepalLengthCm"].to_list()

plt.plot(id_list,sepal_length_list, color =  'green')
plt.xlabel("Id's of species")
plt.ylabel("Sepal lengths in cm")
plt.show()