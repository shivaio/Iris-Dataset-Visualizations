import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")

sepal_length_list = df["SepalLengthCm"].to_list()

sepal_width_list = df["SepalWidthCm"].to_list()

petal_length_list = df['PetalLengthCm'].to_list()

petal_width_list = df['PetalWidthCm'].to_list()

fig1 = plt.figure(figsize =(10, 7))
plt.boxplot(sepal_length_list)
plt.show()

fig2 = plt.figure(figsize =(10, 7))
plt.boxplot(sepal_width_list)
plt.show()

fig3 = plt.figure(figsize =(10, 7))
plt.boxplot(petal_length_list)
plt.show()

fig4 = plt.figure(figsize =(10, 7))
plt.boxplot(petal_width_list)
plt.show()