import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")

species_list = list(set(list(df[:]['Species'])))
print(species_list)
species_count_dict = dict(df[:]["Species"].value_counts())
print(species_count_dict)


species_count = list(species_count_dict.values())

colors = ['green', 'orange', 'red']

explode = (0.05, 0.05, 0.05)


plt.pie(species_count, colors=colors, labels=species_list,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

fig.gca().add_artist(centre_circle)

plt.title("species and their count in dataset")

plt.show()