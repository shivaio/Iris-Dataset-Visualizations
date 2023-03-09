import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")

sepal_length_list = df["SepalLengthCm"].to_list()

sepal_width_list = df["SepalWidthCm"].to_list()

petal_length_list = df['PetalLengthCm'].to_list()

petal_width_list = df['PetalWidthCm'].to_list()

plt.hist(sepal_length_list,color = 'green', bins = 20)
plt.xlabel("Bins")
plt.ylabel("Frequency Count")
plt.legend("Sepal length Histogram ")
plt.show()

plt.hist(sepal_width_list,color = 'green', bins = 20)
plt.xlabel("Bins")
plt.ylabel("Frequency Count")
plt.legend("Sepal width Histogram ")
plt.show()

plt.hist(petal_length_list,color = 'green', bins = 20)
plt.xlabel("Bins")
plt.ylabel("Frequency Count")
plt.legend("petal length Histogram ")
plt.show()

plt.hist(petal_width_list,color = 'green', bins = 20)
plt.xlabel("Bins")
plt.ylabel("Frequency Count")
plt.legend("petal width Histogram ")
plt.show()
