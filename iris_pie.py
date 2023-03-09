import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")

species_list = list(set(list(df[:]['Species'])))
print(species_list)
species_count_dict = dict(df[:]["Species"].value_counts())
print(species_count_dict)


species_count = list(species_count_dict.values())

plt.pie(species_count, labels = species_list,autopct='%1.1f%%')
plt.legend()
plt.show()