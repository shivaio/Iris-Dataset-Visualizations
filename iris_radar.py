import matplotlib.pyplot as plt
import pandas as pd
from math import pi


df = pd.read_csv("Iris.csv")

species_list = list(df[:]['Species'])

sepal_length_list = df["SepalLengthCm"].to_list()

sepal_width_list = df["SepalWidthCm"].to_list()

petal_length_list = df['PetalLengthCm'].to_list()

petal_width_list = df['PetalWidthCm'].to_list()

print(len(sepal_length_list))

print(len(sepal_width_list))

print(len(petal_length_list))

print(len(petal_width_list))



df = pd.DataFrame({
    'group': species_list,
    'var1': sepal_length_list,
    'var2': sepal_width_list,
    'var3': petal_length_list,
    'var4': petal_width_list,
})

print(df)


categories = list(df)[1:]
N = len(categories)


values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]


angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]


ax = plt.subplot(111, polar=True)

plt.xticks(angles[:-1], categories, color='grey', size=8)


ax.set_rlabel_position(0)
plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.ylim(0, 40)


ax.plot(angles, values, linewidth=1, linestyle='solid')


ax.fill(angles, values, 'b', alpha=0.1)


plt.show()